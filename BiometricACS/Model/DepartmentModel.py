from sqlalchemy import NVARCHAR, INTEGER, ForeignKey
from sqlalchemy.schema import Column
from sqlalchemy.ext.hybrid import hybrid_property
from . import Base


class Department(Base):
    __tablename__ = 'department'

    _id = Column('id', INTEGER, primary_key=True)
    _name = Column('name', NVARCHAR(250), nullable=False)
    _cheif_id = Column('cheif_id', INTEGER, ForeignKey('employee.id'), nullable=False)

    @hybrid_property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value not in [None, '']:
            self._cheif_id = value

    @hybrid_property
    def cheif_id(self):
        return self._cheif_id

    @cheif_id.setter
    def cheif_id(self, value):
        if value > 0:
            self._cheif_id = value

    def __repr__(self):
        return "<Department(id='%d', name='%s', cheif_id='%d')>" % (self.id, self.name, self.cheif_id)
