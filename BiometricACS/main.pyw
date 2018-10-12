import sys
import os
import pickle
from PyQt5.QtWidgets import QApplication
from BiometricACS.APP import *
from BiometricACS.BLL.Services import AuthorizationService
from BiometricACS.APP.Controllers import LoginPanelController


def main():
    setup_settings()
    app = QApplication(sys.argv)
    LoginPanelController(AuthorizationService())
    sys.exit(app.exec_())


def setup_settings():
    o_path_default = '.\APP\Sources\Options'
    s_file_default = '.\APP\Sources\Settings'
    l_path_default = 'APP\Sources\Logs'

    if not os.path.exists(o_path_default):
        with open(o_path_default, 'wb') as f:
            pickle.dump(s_file_default, f)

    with open(o_path_default, 'rb') as f:
        program_settings.settings_file = pickle.load(f)

    if not os.path.exists(program_settings.settings_file):
        program_settings.settings_file = s_file_default
        program_settings.save()

    program_settings.restore()

    if not program_settings.logs_path:
        program_settings.logs_path = l_path_default
        # if not os.path.exists(program_settings.logs_path):
        #     os.mkdir(program_settings.logs_path)
        program_settings.save()

    if program_settings.logs_path==l_path_default and not os.path.exists(program_settings.logs_path) :
        os.mkdir(program_settings.logs_path)

    if program_settings.logs_saving is None:
        program_settings.logs_saving = False
        program_settings.save()

    if program_settings.logs_saving:
        program_logs.set_log_file(program_settings.logs_path)

    program_logs.start_program_log()
    program_logs.start()


if __name__ == '__main__':
    main()
