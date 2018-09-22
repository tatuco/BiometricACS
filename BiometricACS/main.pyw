from PyQt5.QtWidgets import QApplication
from BiometricACS.Controller.LoginPanelController import LoginPanelController
from BiometricACS.Model.LoginPanelModel import LoginPanelModel
import sys

def Main():
    app = QApplication(sys.argv)

    login_model = LoginPanelModel()
    login_controller = LoginPanelController(login_model)
    app.exec()

if __name__ == '__main__':
    Main()
