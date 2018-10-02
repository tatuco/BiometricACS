from .BaseDTO import BaseDTO


class ChekpointDTO(BaseDTO):

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if value not in [None, '']:
            self._address = value

    def __init__(self, addess=None):
        self._id = None
        self.address = addess
