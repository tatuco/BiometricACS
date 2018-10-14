from sqlalchemy import VARCHAR, INTEGER
from sqlalchemy.schema import Column
from sqlalchemy.ext.hybrid import hybrid_property
from .BaseEntity import BaseEntity, Base


class Checkpoint(Base, BaseEntity):
    __tablename__ = 'checkpoint'

    _id = Column('id', INTEGER, primary_key=True)
    _address = Column('address', VARCHAR, nullable=False)

    @hybrid_property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if value not in [None, '']:
            self._address = value