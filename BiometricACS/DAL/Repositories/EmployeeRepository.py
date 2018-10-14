from zope.interface import implements, implementer, classImplements, provider
from .BaseRepository import BaseRepository
from ..Entities.Employee import Employee
from ..Interfaces.IRepository import IRepository


@implementer(IRepository)
@provider(IRepository)
class EmployeeRepository(BaseRepository):

    def __init__(self, context):
        self._db = context
        self._type = Employee

    def get_all(self):
        return self._db.Employee.all()

    def get(self, item_id):
        return self._db.Employee.filter(Employee.id == item_id).first()

    def find(self, predicate):
        return self._db.Employee.filter(*predicate).all()
