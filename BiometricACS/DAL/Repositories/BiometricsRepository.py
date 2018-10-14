from zope.interface import implements, implementer, classImplements, provider
from .BaseRepository import BaseRepository
from ..Entities.Biometrics import Biometrics
from ..Interfaces.IRepository import IRepository


@implementer(IRepository)
@provider(IRepository)
class BiometricsRepository(BaseRepository):

    def __init__(self, context):
        self._db = context
        self._type = Biometrics

    def get_all(self):
        return self._db.Biometrics.all()

    def get(self, item_id):
        return self._db.Biometrics.filter(Biometric.id == item_id).first()

    def find(self, predicate):
        return self._db.Biometrics.filter(*predicate).all()