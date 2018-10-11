from . import AuthorizationService
from .BaseService import BaseService


class MainService(BaseService):

    def relogin(self, user):
        self.relogin_service.user = user

    def __init__(self, user=None):
        super().__init__()
        self.relogin_service = AuthorizationService(user)
        pass