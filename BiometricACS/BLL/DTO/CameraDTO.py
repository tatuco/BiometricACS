from .BaseDTO import BaseDTO
from .EnumsDTO import CamerasVectorDTO


class CameraDTO(BaseDTO):

    @property
    def vector(self):
        return self._vector

    @vector.setter
    def vector(self, value):
        if value in list(CamerasVectorDTO):
            self._vector = value

    @property
    def device_name(self):
        return self._device_name

    @device_name.setter
    def device_name(self, value):
        if value not in [None, '']:
            self._device_name = value

    @property
    def ckpt_id(self):
        return self._ckpt_id

    @ckpt_id.setter
    def ckpt_id(self, value):
        if value > 0:
            self._ckpt_id = value

    def __init__(self, vector=None, device_name=None, ckpt_id=None):
        self._id = None
        self._vector = vector
        self._device_name = device_name
        self._ckpt_id = ckpt_id
