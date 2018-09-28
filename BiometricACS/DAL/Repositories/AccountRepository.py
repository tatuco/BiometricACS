from zope.interface import implements, implementer, classImplements, provider
from ..Entities.Account import Account
from ..Interfaces.IRepository import IRepository


@implementer(IRepository)
@provider(IRepository)
class AccountRepository(object):

    def __init__(self, context):
        self.db = context

    def get_all(self):
        return self.db.Account.all()

    def get(self, item_id):
        return self.db.Account.filter(Account.id == item_id).first()

    def find(self, predicate):
        return self.db.Account.filter(predicate).all()

    def create(self, item):
        self.db.sess.add(item)

    def update(self, item):
        self.get(item.id).update(item)

    def delete(self, item):
        self.db.sess.delete(item)
