import os
import logging
from datetime import datetime
from .Log import Log


class ProgramLogging:

    @property
    def logs(self):
        return self._logs

    def start_program_log(self):
        log = Log.get_start_log(self._printing)
        self._execute(log, logging.INFO)

    def login_log(self, username):
        log = Log.get_login_log(self._printing, username)
        self._execute(log, 23)

    def relogin_log(self, username):
        log = Log.get_relogin_log(self._printing, username)
        self._execute(log, 23)

    def bad_login_log(self, username):
        log = Log.get_bad_login_log(self._printing, username)
        self._execute(log, logging.WARNING)

    def close_log(self):
        log = Log.get_close_log(self._printing)
        self._execute(log, logging.INFO)

    def visit_log(self, f_name, l_name, checkpoint):
        log = Log.get_visit_log(self._printing, f_name, l_name, checkpoint)
        self._execute(log, 23)

    def camera_turned_off_log(self, checkpoint, camera):
        log = Log.get_camera_turned_off_log(self._printing, checkpoint, camera)
        self._execute(log, logging.WARNING)

    def camera_turned_on_log(self, checkpoint, camera):
        log = Log.get_camera_turned_on_log(self._printing, checkpoint, camera)
        self._execute(log, 27)

    def create_account_log(self, username):
        log = Log.get_create_account_log(self._printing, username)
        self._execute(log, logging.INFO)

    def export_accounts(self, file_name):
        log = Log.get_export_accounts_log(self._printing, file_name)
        self._execute(log, 27)

    def export_logs_log(self, file_name):
        log = Log.get_export_logs_log(self._printing, file_name)
        self._execute(log, logging.INFO)

    def add_checkpoint_log(self, address):
        log = Log.get_add_checkpoint_log(self._printing, address)
        self._execute(log, 27)

    def add_camera_log(self, device, vector, address):
        log = Log.get_add_camera_log(self._printing, device, vector, address)
        self._execute(log, 27)

    def change_checkpoint_address_log(self, old_address, new_address):
        log = Log.get_change_checkpoint_address_log(self._printing, old_address, new_address)
        self._execute(log, 27)

    def delete_camera_log(self, device, vector, address):
        log = Log.get_delete_camera_log(self._printing, device, vector, address)
        self._execute(log, logging.WARNING)

    def delete_checkpoint_log(self, address):
        log = Log.get_delete_checkpoint_log(self._printing, address)
        self._execute(log, logging.WARNING)
        
    def restart_log(self):
        log = Log.get_restart_log(self._printing)
        self._execute(log, logging.INFO)
        
    def change_settings_log(self):
        log = Log.get_change_settings_log(self._printing)
        self._execute(log, logging.WARNING)

    def save_statistics_log(self, file):
        log = Log.get_save_statistics_log(self._printing, file)
        self._execute(log, logging.INFO)

    def save(self, save_path):
        with open(os.path.join(save_path, str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.log'), 'w') as f:
            for i, log in enumerate(self._logs):
                f.writelines('%d %s %s\n' % (i + 1, log.level, log))

    def set_log_file(self, save_path):
        logging.basicConfig(filename=os.path.join(save_path, str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.log'))
        
    def _execute(self, log, level):
        self._logger.log(level, log.event)
        self._logs.append(log)
        self._handler(log)

    def reset_handler(self, handler):
        self._handler = handler
        self._handler(self._logs)

    def reset_printing(self, printing):
        self._printing = printing

    def __init__(self, handler, printing=True):
        self._handler = handler
        self._printing = printing
        self._logs = []
        # self._formatter = logging.Formatter('%(levelname)s: %(asctime)s %(message)s')
        logging.addLevelName(27, 'IMP_INFO')
        logging.addLevelName(23, 'ACCESS')
        self._logger = logging.getLogger('BACS')
        self._logger.setLevel(logging.INFO)
