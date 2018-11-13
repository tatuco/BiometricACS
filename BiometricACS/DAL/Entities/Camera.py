from sqlalchemy import VARCHAR, INTEGER, Enum, ForeignKey
from sqlalchemy.schema import Column
from sqlalchemy.ext.hybrid import hybrid_property
from .BaseEntity import BaseEntity, Base
from ..Entities.EnumModels import CamerasVector


class Camera(Base, BaseEntity):
    __tablename__ = 'camera'

    _id = Column('id', INTEGER, primary_key=True)
    _vector = Column('vector', Enum(CamerasVector), nullable=False)
    _device_name = Column('device_name', VARCHAR, unique=True)
    _ckpt_id = Column('ckpt_id', INTEGER, ForeignKey('checkpoint.id'), nullable=False)

    @hybrid_property
    def vector(self):
        return self._vector

    @vector.setter
    def vector(self, value):
        if value in list(CamerasVector):
            self._vector = value

    @hybrid_property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        if value not in [None, '']:
            self._device_name = value

    @hybrid_property
    def ckpt_id(self):
        return self._ckpt_id

    @ckpt_id.setter
    def ckpt_id(self, value):
        if value > 0:
            self._ckpt_id = value