from PyQt5 import QtCore
from ..Views import LoginPanelView
from ...BLL.DTO import AccountDTO


class LoginPanelController():

    def __init__(self, imModel):
        self.mModel = imModel
        self.mView = LoginPanelView(self.mModel, self)
        self.mView.show()

    def entetr_clicled(self, event):
        if event.key() + 1 == QtCore.Qt.Key_Enter:
            self.login_clicked()

    def login_clicked(self):
        username = self.mView.ui.tbUsername.text()
        password = self.mView.ui.tbPassword.text()
        self.mModel.user = AccountDTO(username, password)

    def cancel_clicked(self):
        exit(0)

    def is_registred(self):
        return self.mModel.is_registred(self.mModel.user)
