from PyQt5 import QtCore
from ..Views import LoginPanelView
from ...BLL.DTO import AccountDTO
from ..AppStart import program_logs, datetime, Log
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
            log = Log(datetime.now(), "Login as '%s'" % user.username)
            print(log)
            program_logs.add_log(log)

            self.view_close()
            main_controller = MainController(MainService(user), self.view)
        else:
            log = Log.get_bad_login_log(self.view.ui.tbUsername.text())
