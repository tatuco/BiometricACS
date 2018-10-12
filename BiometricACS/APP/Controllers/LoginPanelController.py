from PyQt5 import QtCore
from ..Views import LoginPanelView
from ...BLL.DTO import AccountDTO
from ..AppStart import program_logs
from ..Controllers import MainController
from ...BLL.Services import MainService


class LoginPanelController:

    def __init__(self, inModel):
        self.model = inModel
        self.view = LoginPanelView(self.model, self)
        self.view.show()

    def enter_clicked(self, event):
        if event.key() + 1 == QtCore.Qt.Key_Enter:
            self.login_clicked()

    def login_clicked(self):
        username = self.view.ui.tbUsername.text()
        password = self.view.ui.tbPassword.text()
        self.model.user = AccountDTO(username, password)

    def is_registred(self):
        return self.model.is_registred(self.model.user)

    def cancel_clicked(self):
        self.view_close()

    def view_close(self):
        self.view.close()

    def main(self):
        result, user = self.is_registred()
        if result:
            program_logs.login_log(user.username)

            self.view_close()
            main_controller = MainController(MainService(user), self.view)
        else:
            log = program_logs.bad_login_log(self.view.ui.tbUsername.text())
