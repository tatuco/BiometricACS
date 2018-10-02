from zope.interface import implements, implementer, classImplements, provider
from .BaseRepository import BaseRepository
from ..Entities.Account import Account
from ..Interfaces.IRepository import IRepository


@implementer(IRepository)
@provider(IRepository)
class AccountRepository(BaseRepository):

    def __init__(self, context):
        self._db = context
        self._type = Account

    def get_all(self):
        return self._db.Account.all()

    def get(self, item_id):
        return self._db.Account.filter(Account.id == item_id).first()

    def find(self, predicate):
        return self._db.Account.filter(*predicate).all()