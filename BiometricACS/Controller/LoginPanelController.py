from BiometricACS.View.LoginPanelView import LoginPanenView
from PyQt5 import QtCore


class LoginPanelController():

    def __init__(self, imModel):
        self.mModel = imModel
        self.mView = LoginPanenView(self.mModel, self)
        self.mView.show()

    def entetrClicled(self, event):
        if event.key() + 1 == QtCore.Qt.Key_Enter:
            self.loginClicked()

    def loginClicked(self):
        username = self.mView.ui.tbUsername.text()
        password = self.mView.ui.tbPassword.text()
        self.mModel.user = [username, password]

    def cancelClicked(self):
        exit(0)
