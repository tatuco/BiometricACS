from PyQt5 import QtCore
from ..Views import ReloginPanelView
from ..AppStart import program_logs, datetime, Log
from ...BLL import AccountDTO


class ReloginPanelController:

    def __init__(self, in_model, parent=None):
        self.parent = parent
        self.model = in_model
        self.view = ReloginPanelView(in_model, self, parent)
        self.view.show()

    def enter_clicked(self, event):
        if event.key() + 1 == QtCore.Qt.Key_Enter:
            self.login_clicked()

    def login_clicked(self):
        username = self.view.ui.tbUsername.text()
        password = self.view.ui.tbPassword.text()
        self.model.user = AccountDTO(username, password)

    def cancel_clicked(self):
        self.view.close()

    def is_registred(self):
        return self.model.is_registred(self.model.user)

    def relogin(self):
        result, user = self.is_registred()
        if result:
            program_logs.add_log(Log.get_relogin_log(user.username))
            self.view.parent_o.model_is_changed()
            self.view.close()
