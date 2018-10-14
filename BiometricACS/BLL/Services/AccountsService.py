from .BaseService import BaseService
from ..DTO import AccountDTO, AccountRoleDTO
from ...DAL import Account, EntitiesUnit


class AccountsService(BaseService):

    @property
    def accounts(self):
        return [AccountDTO().update(i) for i in self.db.get_all()]

    def relogin(self, user):
        self.relogin_service.user = user

    def create_account(self, user):
        self.db.create(user)
        self.rep.save()

    def is_exists(self, username):
        result = self.db.find((Account.username == username,))
        return True if len(result) > 0 else False

    def __init__(self, connection_string):
        super().__init__()
        self.rep = EntitiesUnit(connection_string)
        self.db = self.rep.account_repository