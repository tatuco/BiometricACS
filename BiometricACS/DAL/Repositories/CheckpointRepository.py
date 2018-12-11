from zope.interface import implements, implementer, classImplements, provider

from .BaseRepository import BaseRepository
from ..Entities.Checkpoint import Checkpoint
from ..Interfaces.IRepository import IRepository


@implementer(IRepository)
@provider(IRepository)
class CheckpointRepository(BaseRepository):

    def __init__(self, context):
        self._db = context
        self._type = Checkpoint

    def get_all(self):
        return self._db.Checkpoint.all()

    def get(self, item_id):
        return self._db.Checkpoint.filter(Checkpoint.id == item_id).first()

    def find(self, predicate):
        return self._db.Checkpoint.filter(*predicate).all()