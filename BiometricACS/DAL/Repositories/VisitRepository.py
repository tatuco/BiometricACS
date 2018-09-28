from zope.interface import implements, implementer, classImplements, provider
from ..Entities.Visit import Visit
from ..Interfaces.IRepository import IRepository


@implementer(IRepository)
@provider(IRepository)
class VisitRepository(object):

    def __init__(self, context):
        self.db = context

    def get_all(self):
        return self.db.Visit.all()

    def get(self, item_id):
        return self.db.Visit.filter(Visit.id == item_id).first()

    def find(self, predicate):
        return self.db.Visit.filter(predicate).all()

    def create(self, item):
        self.db.sess.add(item)

    def update(self, item):
        self.get(item.id).update(item)

    def delete(self, item):
        self.db.sess.delete(item)
