import logging
import os
from datetime import datetime
import threading
from .Log import Log


class ProgramLogging(threading.Thread):

    @property
    def logs(self):
        return self._logs

    def start_program_log(self):
        log = Log.get_start_log(self._printing)
        self._logger.log(logging.INFO, log.event)
        self._logs.append(log)
        self._handler(log)

    def login_log(self, username):
        log = Log.get_login_log(self._printing, username)
        self._logger.log(logging.INFO, log.event)
        self._logs.append(log)
        self._handler(log)

    def relogin_log(self, username):
        log = Log.get_relogin_log(self._printing, username)
        self._logger.log(logging.INFO, log.event)
        self._logs.append(log)
        self._handler(log)

    def bad_login_log(self, username):
        log = Log.get_bad_login_log(self._printing, username)
        self._logger.log(logging.INFO, log.event)
        self._logs.append(log)
        self._handler(log)

    def close_log(self):
        log = Log.get_close_log(self._printing)
        self._logger.log(logging.INFO, log.event)
        self._logs.append(log)
        self._handler(log)

    def visit_log(self, f_name, l_name, checkpoint):
        log = Log.get_visit_log(self._printing, f_name, l_name, checkpoint)
        self._logger.log(logging.INFO, log.event)
        self._logs.append(log)
        self._handler(log)

    def camera_turned_off_log(self, checkpoint, camera):
        log = Log.get_camera_turned_off_log(self._printing, checkpoint, camera)
        self._logger.log(logging.WARNING, log.event)
        self._logs.append(log)
        self._handler(log)

    def save(self, save_path):
        with open(os.path.join(save_path, str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.log'), 'w') as f:
            for i, log in enumerate(self._logs):
                f.writelines('%d %s %s\n' % (i + 1, log.level, log))

    def set_log_file(self, save_path):
        logging.basicConfig(filename=os.path.join(save_path, str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.log'))

    def reset_handler(self, handler):
        self._handler = handler
        self._handler(self._logs)

    def reset_printing(self, printing):
        self._printing = printing

    def __init__(self, handler, printing=True):
        threading.Thread.__init__(self, name='LoggingThread')
        self._handler = handler
        self._printing = printing
        self._logs = []
        # self._formatter = logging.Formatter('%(levelname)s: %(asctime)s %(message)s')
        self._logger = logging.getLogger('BACS')
        self._logger.setLevel(logging.INFO)
