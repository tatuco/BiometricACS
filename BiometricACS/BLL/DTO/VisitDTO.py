from .BaseDTO import BaseDTO


class VisitDTO(BaseDTO):

    @property
    def datetime(self):
        return self._date_time

    @datetime.setter
    def datetime(self, value):
        self._date_time = value

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value

    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        if value > 0:
            self._emp_id = value

    @property
    def camera_id(self):
        return self._camera_id

    @camera_id.setter
    def camera_id(self, value):
        if value > 0:
            self._camera_id = value

    def __init__(self, date_time=None, event=None, emp_id=None, camera_id=None):
        self._id = None
        self._date_time = date_time
        self._event = event
        self._emp_id = emp_id
        self._camera_id = camera_id
