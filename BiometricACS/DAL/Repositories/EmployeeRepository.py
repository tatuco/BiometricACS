from zope.interface import implements, implementer, classImplements, provider
from ..Entities.Employee import Employee
from ..Interfaces.IRepository import IRepository


@implementer(IRepository)
@provider(IRepository)
class EmployeeRepository(object):

    def __init__(self, context):
        self.db = context

    def get_all(self):
        return self.db.Employee.all()

    def get(self, item_id):
        return self.db.Employee.filter(Employee.id == item_id).first()

    def find(self, predicate):
        return self.db.Employee.filter(predicate).all()

    def create(self, item):
        self.db.sess.add(item)

    def update(self, item):
        self.get(item.id).update(item)

    def delete(self, item):
        self.db.sess.delete(item)
