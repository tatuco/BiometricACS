from .BaseService import BaseService
from ..DTO import AccountDTO, AccountRoleDTO
from ..Infrastructure.ServiceModule import connection_string
from ...DAL import Account, EntitiesUnit


class AuthorizationService(BaseService):

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        assert isinstance(value, AccountDTO)
        cond_l = [None, '']
        if value and value.username not in cond_l and value.password not in cond_l and value.username != self._user.username or value.password != self._user.password:
            self._user = value
            self.notify_observers()

    def is_registred(self, user):
        db = EntitiesUnit(connection_string).account_repository
        result = db.find((Account.username == user.username, Account.password == user.password))
        if result:
            return True, AccountDTO().update(result[0])
        return False, None

    def __init__(self):
        self._user = AccountDTO('', '')