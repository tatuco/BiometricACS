from PyQt5.QtWidgets import QApplication
from BiometricACS.APP.Controller.LoginPanelController import LoginPanelController
from BiometricACS.DAL.Entities.Account import Account
import sys


def Main():
    app = QApplication(sys.argv)

    login_model = Account()
    login_controller = LoginPanelController(login_model)
    app.exec()


if __name__ == '__main__':
    Main()
