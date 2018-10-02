from .BaseDTO import BaseDTO
from .EnumsDTO import EmployeeStatusDTO


class EmployeeDTO(BaseDTO):

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if value not in [None, '']:
            self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if value not in [None, '']:
            self._last_name = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value in list(EmployeeStatusDTO):
            self._status = value

    @property
    def dept_id(self):
        return self._dept_id

    @dept_id.setter
    def dept_id(self, value):
        self._dept_id = value

    def __init__(self, first_name=None, last_name=None, status=None, dept_id=None):
        self._id = None
        self._first_name = first_name
        self._last_name = last_name
        self._status = status
        self._dept_id = dept_id
