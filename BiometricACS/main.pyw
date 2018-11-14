import sys
import os
import pickle
import gettext
import builtins
from PyQt5 import QtGui, QtCore
from PyQt5.Qt import QTranslator, QLocale
from PyQt5.QtWidgets import QApplication, QInputDialog, QMessageBox, QWidget

from BiometricACS.APP import *
from BiometricACS.DAL import EntitiesUnit
from BiometricACS.BLL.Services import AuthorizationService
from BiometricACS.APP.Controllers import LoginPanelController


def exeption_hook(exctype, value, tracekack):
    print(exctype, value, tracekack)
    sys.__excepthook(exctype, value, tracekack)
    sys.exit(1)


def main():
    app = QApplication(sys.argv)

    setup_settings()

    translator = setup_locale(program_settings.language)
    app.installTranslator(translator)

    program_logs.start_program_log()
    LoginPanelController(AuthorizationService(program_settings.connection_string))
    sys.exit(app.exec_())


def setup_settings():

    if not os.path.exists(program_settings.cfg_file):
        with open(program_settings.cfg_file, 'wb') as f:
            pickle.dump(program_settings.settings_file, f)

    with open(program_settings.cfg_file, 'rb') as f:
        program_settings.settings_file = pickle.load(f)

    if not os.path.exists(program_settings.settings_file):
        open(program_settings.settings_file, 'w').close()
        program_settings.save()

    program_settings.restore()

    if not os.path.exists(program_settings.logs_path):
        os.mkdir(program_settings.logs_path)

    if program_settings.logs_saving is None:
        program_settings.logs_saving = False
        program_settings.save()

    if program_settings.logs_saving:
        program_logs.set_log_file(program_settings.logs_path)

    if not program_settings.connection_string:
        setup_connection_string()


def setup_connection_string():
    dialog = QInputDialog()
    icon_widget = QWidget()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(r".\APP\Sources\Icons\Program.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    icon_widget.setWindowIcon(icon)
    text, ok = dialog.getText(icon_widget, 'Connection string', 'Enter the connection string to your database:')
    if ok:
        if EntitiesUnit.is_valid_connection(text):
            program_settings.connection_string = text
            program_settings.save()
        else:
            try_again = QMessageBox().question(None, 'Invalid connection', 'Database doesnt exists or username/password incorrect\nTry again?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if try_again == QMessageBox.Yes:
                setup_connection_string()
            else:
                quit()
    else:
        quit()


def setup_locale(lang):
    locale = '.\APP\Locale'
    domain = 'messages'

    t = gettext.translation(domain, locale, languages=[lang])
    _ = t.gettext
    builtins.__dict__['_'] = _
    builtins.__dict__['gettext'] = builtins.__dict__['_']

    translator = QTranslator()
    translator.load(r"ui.qm", locale+r"\%s\LC_MESSAGES"%lang)
    return translator


if __name__ == '__main__':
    sys.__excepthook = sys.excepthook
    sys.excepthook = exeption_hook
    main()
