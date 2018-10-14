from zope.interface import implements, implementer, classImplements, provider
from .BaseRepository import BaseRepository
from ..Entities.Camera import Camera
from ..Interfaces.IRepository import IRepository


@implementer(IRepository)
@provider(IRepository)
class CameraRepository(BaseRepository):

    def __init__(self, context):
        self._db = context
        self._type = Camera

    def get_all(self):
        return self._db.Camera.all()

    def get(self, item_id):
        return self._db.Camera.filter(Camera.id == item_id).first()

    def find(self, predicate):
        return self._db.Camera.filter(*predicate).all()