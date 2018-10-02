from zope.interface import implements, implementer, classImplements, provider
from .BaseRepository import BaseRepository
from ..Entities.Department import Department
from ..Interfaces.IRepository import IRepository


@implementer(IRepository)
@provider(IRepository)
class DepartmentRepository(BaseRepository):

    def __init__(self, context):
        self.db = context

    def get_all(self):
        return self.db.Department.all()

    def get(self, item_id):
        return self.db.Department.filter(Department.id == item_id).first()

    def find(self, predicate):
        return self.db.Department.filter(*predicate).all()