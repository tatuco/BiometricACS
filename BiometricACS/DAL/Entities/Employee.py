from sqlalchemy import NVARCHAR, INTEGER, Enum, ForeignKey
from sqlalchemy.schema import Column
from sqlalchemy.ext.hybrid import hybrid_property
from .BaseEntity import BaseEntity, Base
from ..Entities.EnumModels import EmployeeStatus


class Employee(Base):
    __tablename__ = 'employee'

    _id = Column('id', INTEGER, primary_key=True)
    _first_name = Column('first_name', NVARCHAR(250), nullable=False)
    _last_name = Column('last_name', NVARCHAR(250), nullable=False)
    _status = Column('status', Enum(EmployeeStatus), nullable=False)
    _dept_id = Column('dept_id', INTEGER, ForeignKey('employee.id'), nullable=False)

    @hybrid_property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value not in [None, '']:
            self._first_name = value

    @hybrid_property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value not in [None, '']:
            self._last_name = value

    @hybrid_property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value in list(EmployeeStatus):
            self._status = value

    @hybrid_property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value

