from datetime import datetime


class Log:

    @staticmethod
    def get_relogin_log(username, printing=True):
        log = Log(datetime.now(), "Relogin as '%s'" % username)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_bad_login_log(username, printing=True):
        log = Log(datetime.now(), "Failed login as '%s'" % username)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_close_log(printing=True):
        log = Log(datetime.now(), "The program has completed its work." )
        if printing:
            print(log)
        return log

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
