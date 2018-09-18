from PyQt5.QtWidgets import QApplication
from BiometricACS.Controller.LoginPanelController import LoginPanelController
import sys

def Main():
    app = QApplication(sys.argv)

    model = None
    controller = LoginPanelController(model)

    app.exec()

if __name__ == '__main__':
    Main()
