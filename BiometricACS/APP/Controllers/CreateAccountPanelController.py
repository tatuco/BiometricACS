from PyQt5.QtWidgets import QMessageBox

from ..Views import CreateAccountPanelView
from ..AppStart import program_logs
from ...BLL.DTO import AccountDTO, AccountRoleDTO


class CreateAccountPanelController:

    def __init__(self, in_model, parent=None):
        self.model = in_model
        self.view = CreateAccountPanelView(in_model, self, parent)

        self.view.set_combobox_items([i.value for i in AccountRoleDTO])
        self.view.show()

    def create_clicked(self):
        if self.view.ui.tbUsername.text() == '':
            QMessageBox.warning(self.view, 'Warning', 'Enter username')
            return
        if self.model.is_exists(self.view.ui.tbUsername.text()):
            QMessageBox.warning(self.view, 'Warning', 'Such account already exists')
            return
        if self.view.ui.tbPassword.text() == '':
            QMessageBox.warning(self.view, 'Warning', 'Enter password')
            return
        if self.view.ui.tbPassword.text() != self.view.ui.tbConfirmPassword.text():
            QMessageBox.warning(self.view, 'Warning', 'Passwords do not match')
            return
        acc = AccountDTO()
        acc.username = self.view.ui.tbUsername.text()
        acc.role = list(AccountRoleDTO)[self.view.ui.cmbRole.currentIndex()]
        acc.password = self.view.ui.tbPassword.text()
        self.model.create_account(acc)
        QMessageBox.information(self.view, 'Success', 'Account created successfully')
        self.view.close()
        program_logs.create_account_log(acc.username)
