from datetime import datetime

from .LogLevels import LogLevels


class Log:

    @staticmethod
    def get_start_log(printing):
        log = Log(datetime.now(), _("Initialize program components"), LogLevels.INFO)
        if printing:
            print(log)
        return log


    @staticmethod
    def get_login_log(printing, username):
        log = Log(datetime.now(), _("Login as '%s'") % username, LogLevels.ACCESS)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_relogin_log(printing, username):
        log = Log(datetime.now(), _("Relogin as '%s'") % username, LogLevels.ACCESS)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_bad_login_log(printing, username):
        log = Log(datetime.now(), _("Failed login as '%s'") % username, LogLevels.WARNING)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_close_log(printing):
        log = Log(datetime.now(), _("The program has completed its work."), LogLevels.INFO)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_visit_log(printing, f_name, l_name, checkpoint):
        log = Log(datetime.now(), _("'%s %s' was given the access on '%s'") % (f_name, l_name, checkpoint), LogLevels.ACCESS)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_camera_turned_off_log(printing, checkpoint, camera):
        log = Log(datetime.now(), _("Camera '%s' on '%s' turned off") % (camera, checkpoint), LogLevels.WARNING)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_camera_turned_on_log(printing, checkpoint, camera):
        log = Log(datetime.now(), _("Camera '%s' has restored its work on '%s'") % (camera, checkpoint), LogLevels.IMP_INFO)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_create_account_log(printing, username):
        log = Log(datetime.now(), _("Account '%s' created") % username, LogLevels.INFO)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_export_accounts_log(printing, file_name):
        log = Log(datetime.now(), _("Export accounts to file '%s'") % file_name, LogLevels.IMP_INFO)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_export_logs_log(printing, file_name):
        log = Log(datetime.now(), _("Export session log to file '%s'") % file_name, LogLevels.INFO)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_add_checkpoint_log(printing, address):
        log = Log(datetime.now(), _("Added checkpoint '%s'") % address, LogLevels.IMP_INFO)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_add_camera_log(printing, device, vector, address):
        log = Log(datetime.now(), _("Added device '%s' aimed at '%s' on '%s'") % (device, vector, address), LogLevels.IMP_INFO)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_change_checkpoint_address_log(printing, old_address, new_address):
        log = Log(datetime.now(), _("Changed checkpoint address '%s' -> '%s'") % (old_address, new_address), LogLevels.IMP_INFO)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_delete_camera_log(printing, device, vector, address):
        log = Log(datetime.now(), _("Camera removed: '%s' device, '%s' vector, on '%s'") % (device, vector, address), LogLevels.WARNING)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_delete_checkpoint_log(printing, address):
        log = Log(datetime.now(), _("Checkpoint '%s' removed") % address, LogLevels.WARNING)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_restart_log(printing):
        log = Log(datetime.now(), _('Restart'), LogLevels.INFO)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_change_settings_log(printing):
        log = Log(datetime.now(), _('Сhange settings'), LogLevels.WARNING)
        if printing:
            print(log)
        return log

    @staticmethod
    def get_save_statistics_log(printing, file):
        log = Log(datetime.now(), _(f'Save statistics to file: {file}'), LogLevels.INFO)
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
