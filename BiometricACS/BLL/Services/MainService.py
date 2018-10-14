from . import AuthorizationService, AccountsService, CheckpointService
from .BaseService import BaseService


class MainService(BaseService):

    def __init__(self, connection_string, user=None):
        super().__init__()
        self.accounts_service = AccountsService(connection_string)
        self.relogin_service = AuthorizationService(connection_string, user)
        self.checkpoints_service = CheckpointService(connection_string)