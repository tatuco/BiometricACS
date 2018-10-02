from .BaseDTO import BaseDTO


class DepartmentDTO(BaseDTO):

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value not in [None, '']:
            self._name = value

    @property
    def cheif_id(self):
        return self._cheif_id

    @cheif_id.setter
    def cheif_id(self, value):
        if value > 0:
            self._cheif_id = value

    def __init__(self, name=None, cheif_id=None):
        self._id = None
        self._name=name
        self._cheif_id=cheif_id