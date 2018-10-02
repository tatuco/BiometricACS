class Log:

    @property
    def date_time(self):
        return self._datetime

    @date_time.setter
    def date_time(self, value):
        self._datetime = value

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        self._event = value

    def __repr__(self):
        return '%s %s' % (str(self.date_time), self.event)

    def __init__(self, date_time, event):
        self._datetime = date_time
        self._event = event
