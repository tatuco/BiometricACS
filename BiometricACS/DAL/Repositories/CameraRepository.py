from zope.interface import implements, implementer, classImplements, provider
from .BaseRepository import BaseRepository
from ..Entities.Camera import Camera
from ..Interfaces.IRepository import IRepository


@implementer(IRepository)
@provider(IRepository)
class CameraRepository(BaseRepository):

    def __init__(self, context):
        self.db = context

    def get_all(self):
        return self.db.Camera.all()

    def get(self, item_id):
        return self.db.Camera.filter(Camera.id == item_id).first()

    def find(self, predicate):
        return self.db.Camera.filter(*predicate).all()