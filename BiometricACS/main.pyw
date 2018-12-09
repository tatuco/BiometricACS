import sys
import os
import subprocess
import pickle
import gettext
import builtins
from PyQt5 import QtGui, QtCore
from PyQt5.Qt import QTranslator, QLocale
from PyQt5.QtWidgets import QApplication, QInputDialog, QMessageBox, QWidget

from BiometricACS.APP import *
from BiometricACS.BLL import Settings
from BiometricACS.BLL.Services import AuthorizationService
from BiometricACS.APP.Controllers import LoginPanelController
from BiometricACS.APP.Views.BaseView import BaseView

APP = QApplication(sys.argv)

def exeption_hook(exctype, value, tracekack):
    print(exctype, value, tracekack)
    sys.__excepthook(exctype, value, tracekack)
    sys.exit(1)


def main():
    translator = setup_settings()
    APP.installTranslator(translator)

    program_logs.start_program_log()
    LoginPanelController(AuthorizationService(program_settings.connection_string))
    sys.exit(APP.exec_())


def setup_settings():
    if not os.path.exists(program_settings.cfg_file):
        cfg_dir_name = program_settings.cfg_file.replace('\\' + os.path.basename(program_settings.cfg_file), '')
        if not os.path.exists(cfg_dir_name):
            os.mkdir(cfg_dir_name)
        with open(program_settings.cfg_file, 'wb') as f:
            pickle.dump(program_settings.settings_file, f)

    with open(program_settings.cfg_file, 'rb') as f:
        program_settings.settings_file = pickle.load(f)

    if not os.path.exists(program_settings.settings_file):
        open(program_settings.settings_file, 'wb').close()
        program_settings.save()

    result_restore = program_settings.forced_restore(program_settings.settings_file, Settings().settings_file)

    locale = '.\APP\Locale'
    domain = 'messages'
    t = gettext.translation(domain, locale, languages=[program_settings.language])
    _ = t.gettext
    builtins.__dict__['_'] = _
    builtins.__dict__['gettext'] = builtins.__dict__['_']
    translator = QTranslator()
    translator.load(r"ui.qm", locale + r"\%s\LC_MESSAGES" % program_settings.language)

    if not result_restore:
        qmb_file_damaged = QMessageBox()
        BaseView.setup_window_icon(qmb_file_damaged)
        qmb_file_damaged.warning(qmb_file_damaged, _('Warning'), _('Settings file is damaged!\nSettings returned to their previous state.'))

    if not os.path.exists(program_settings.logs_path):
        os.mkdir(program_settings.logs_path)

    if program_settings.logs_saving is None:
        program_settings.logs_saving = False
        program_settings.save()

    if program_settings.logs_saving:
        program_logs.set_log_file(program_settings.logs_path)

    if not program_settings.connection_string:
        setup_connection_string()

    return translator


def setup_connection_string():
    dialog = QInputDialog()
    BaseView.setup_window_icon(dialog)
    text, ok = dialog.getText(dialog, _('Connection string'), _('Enter the connection string to your database:'))
    if ok:
        if program_settings.is_valid_connection(text):
            program_settings.connection_string = text
            program_settings.save()
            account = program_settings.parse_connection_string(text)
            if account:
                qmb_message = QMessageBox()
                BaseView.setup_window_icon(qmb_message)
                qmb_message.information(qmb_message, _('Success'), _(f'Successful creation of a new account!\nLogin:') + account.username + _('\nPassword:') + account.password)
            else:
                qmb_message = QMessageBox()
                BaseView.setup_window_icon(qmb_message)
                qmb_message.information(qmb_message, _('Success'), _('Database successfully integrated, log in under one of the existing accounts'))
        else:
            qmb_message = QMessageBox()
            BaseView.setup_window_icon(qmb_message)
            try_again = qmb_message.question(qmb_message, _('Invalid connection'), _('Database doesnt exists or username/password incorrect\nTry again?'), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if try_again == QMessageBox.Yes:
                setup_connection_string()
            else:
                quit()
    else:
        quit()

def do_restart():
    APP.exit(0)
    subprocess.call([sys.executable, __file__])
    sys.exit(0)

if __name__ == '__main__':
    sys.__excepthook = sys.excepthook
    sys.excepthook = exeption_hook
    builtins.__dict__['do_restart'] = do_restart
    main()
