from .BaseDTO import BaseDTO
from .EnumsDTO import AccountRoleDTO


class AccountDTO(BaseDTO):

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if value not in [None, '']:
            self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if value not in [None, '']:
            self._password = value

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, vale):
        if vale in list(AccountRoleDTO):
            self._role = vale

    def __init__(self, username=None, password=None, role=None):
        self._id = None
        self._username = username
        self._password = password
        self._role = role
