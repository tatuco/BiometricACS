from zope.interface import implements, implementer, classImplements, provider
from .BaseRepository import BaseRepository
from ..Entities.Checkpoint import Checkpoint
from ..Interfaces.IRepository import IRepository


@implementer(IRepository)
@provider(IRepository)
class CheckpointRepository(BaseRepository):

    def __init__(self, context):
        self.db = context

    def get_all(self):
        return self.db.Checkpoint.all()

    def get(self, item_id):
        return self.db.Checkpoint.filter(Checkpoint.id == item_id).first()

    def find(self, predicate):
        return self.db.Checkpoint.filter(*predicate).all()