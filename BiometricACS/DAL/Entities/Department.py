from sqlalchemy import NVARCHAR, INTEGER, ForeignKey
from sqlalchemy.schema import Column
from sqlalchemy.ext.hybrid import hybrid_property

from .BaseEntity import BaseEntity, Base


class Department(Base, BaseEntity):
    __tablename__ = 'department'

    _id = Column('id', INTEGER, primary_key=True)
    _name = Column('name', NVARCHAR(250), nullable=False)
    _chief_id = Column('chief_id', INTEGER, ForeignKey('employee.id'), nullable=False)

    @hybrid_property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value not in [None, '']:
            self._name = value

    @hybrid_property
    def chief_id(self):
        return self._chief_id

    @chief_id.setter
    def chief_id(self, value):
        if value > 0:
            self._chief_id = value