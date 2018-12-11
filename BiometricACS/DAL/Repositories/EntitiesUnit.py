from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError, DBAPIError, ArgumentError
from zope.interface import implementer, provider

from . import *
from ..Interfaces import IEntitiesUnit, IRepository
from ..Contexts import BacsDataContext


@implementer(IEntitiesUnit)
@provider(IEntitiesUnit)
class EntitiesUnit(object):

    @property
    def account_repository(self):
        return IRepository(self._AccountRepository)

    @property
    def biometrics_repository(self):
        return IRepository(self._BiometricsRepository)

    @property
    def camera_repository(self):
        return IRepository(self._CameraRepository)

    @property
    def checkpoint_repository(self):
        return IRepository(self._CheckpointRepository)

    @property
    def employee_repository(self):
        return IRepository(self._EmployeeRepository)

    @property
    def visit_repository(self):
        return IRepository(self._VisitRepository)

    @property
    def department_repository(self):
        return IRepository(self._DepartmentRepository)
    
    @staticmethod
    def is_valid_connection(connection_string):
        try:
            engine = create_engine(connection_string)
            connection = engine.connect()
            connection.close()
        except (ArgumentError, OperationalError):
            return False
        else:
            return True

    def __init__(self, connection_string):
        self._db = BacsDataContext(connection_string)
        self._AccountRepository = AccountRepository(self._db)
        self._BiometricsRepository = BiometricsRepository(self._db)
        self._CameraRepository = CameraRepository(self._db)
        self._CheckpointRepository = CheckpointRepository(self._db)
        self._DepartmentRepository = DepartmentRepository(self._db)
        self._EmployeeRepository = EmployeeRepository(self._db)
        self._VisitRepository = VisitRepository(self._db)

    def save(self):
        self._db.sess.commit()