import sys
import os
import pickle
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QInputDialog, QMessageBox, QWidget
from BiometricACS.APP import *
from BiometricACS.DAL import EntitiesUnit
from BiometricACS.BLL.Services import AuthorizationService
from BiometricACS.APP.Controllers import LoginPanelController
import multiprocessing


def main():
    app = QApplication(sys.argv)
    setup_settings()
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

    program_logs.start_program_log()


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


if __name__ == '__main__':
    main()
