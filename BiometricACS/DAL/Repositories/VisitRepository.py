from zope.interface import implements, implementer, classImplements, provider
from .BaseRepository import BaseRepository
from ..Entities.Visit import Visit
from ..Interfaces.IRepository import IRepository


@implementer(IRepository)
@provider(IRepository)
class VisitRepository(BaseRepository):

    def __init__(self, context):
        self._db = context
        self._type = Visit

    def get_all(self):
        return self._db.Visit.all()

    def get(self, item_id):
        return self._db.Visit.filter(Visit.id == item_id).first()

    def find(self, predicate):
        return self._db.Visit.filter(*predicate).all()
