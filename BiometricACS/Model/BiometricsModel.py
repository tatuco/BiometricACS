from sqlalchemy import NUMERIC, INTEGER, ARRAY, Enum, ForeignKey
from sqlalchemy.schema import Column
from sqlalchemy.ext.hybrid import hybrid_property
from . import Base
from ..Model.EnumModels import CamerasVector


class Biometrics(Base):
    __tablename__ = 'biometrics'

    _id = Column('id', INTEGER, primary_key=True)
    _original_image = Column('original_image', ARRAY(INTEGER, dimensions=3), nullable=False, unique=True)
    _landmarks = Column('landmarks', ARRAY(INTEGER, dimensions=2), nullable=False)
    _features = Column('features', ARRAY(NUMERIC, dimensions=1), nullable=False, unique=True)
    _emp_id = Column('emp_id', INTEGER, ForeignKey('employee.id'), nullable=False)

    @hybrid_property
    def id(self):
        return self._id

    @hybrid_property
    def original_image(self):
        return self._original_image

    @original_image.setter
    def original_image(self, value):
        self._original_image = value

    @hybrid_property
    def landmarks(self):
        return self._landmarks

    @landmarks.setter
    def landmarks(self, value):
        self._landmarks = value

    @hybrid_property
    def features(self):
        return self._features

    @features.setter
    def features(self, value):
        self._features = value

    def __repr__(self):
        return "<Biometrics(id='%d')>" % (self.id)