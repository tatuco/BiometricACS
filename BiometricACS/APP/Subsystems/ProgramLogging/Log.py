from datetime import datetime
from .LogLevels import LogLevels


class Log:

    @staticmethod
    def get_login_log(printing, username):
        log = Log(datetime.now(), "Login as '%s'" % username, LogLevels.ACCESS)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_relogin_log(printing, username):
        log = Log(datetime.now(), "Relogin as '%s'" % username, LogLevels.ACCESS)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_bad_login_log(printing, username):
        log = Log(datetime.now(), "Failed login as '%s'" % username, LogLevels.WARNING)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_close_log(printing):
        log = Log(datetime.now(), "The program has completed its work.", LogLevels.INFO)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_start_log(printing):
        log = Log(datetime.now(), "Initialize program components", LogLevels.INFO)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_visit_log(printing, f_name, l_name, checkpoint):
        log = Log(datetime.now(), "'%s %s' was given the access on '%s'" % (f_name, l_name, checkpoint), LogLevels.ACCESS)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_camera_turned_off_log(printing, checkpoint, camera):
        log = Log(datetime.now(), "Camera '%s' on '%s' turned off" % (camera, checkpoint), LogLevels.WARNING)
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

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    def __repr__(self):
        return '%s %s' % (str(self.date_time), self.event)

    def __init__(self, date_time, event, level):
        self._datetime = date_time
        self._event = event
        self._level = level
