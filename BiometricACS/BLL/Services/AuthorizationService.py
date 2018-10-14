from .BaseService import BaseService
from ..DTO import AccountDTO, AccountRoleDTO
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

    def _get_user(self, user):
        result = self.db.find((Account.username == user.username, Account.password == user.password))
        return AccountDTO().update(result[0]) if result != [] else None

    def is_registred(self, user):
        result = self._get_user(user)
        if result:
            self._user = result
            return True, result
        return False, None

    def __init__(self, connection_string, user=None):
        super().__init__()
        self.db = EntitiesUnit(connection_string).account_repository
        if user:
            self._user = user
        else:
            self._user = AccountDTO('', '')
