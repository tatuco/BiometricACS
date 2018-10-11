import sys
import os
import pickle
from PyQt5.QtWidgets import QApplication
from BiometricACS.APP import *
from BiometricACS.BLL.Services import AuthorizationService
from BiometricACS.APP.Controllers import LoginPanelController


def main():
    log = Log(datetime.now(), 'Initialize program components')
    print(log)
    program_logs.add_log(log)

    o_path_default = '.\APP\Sources\Options'
    s_file_default = '.\APP\Sources\Settings'
    if not os.path.exists(o_path_default):
        with open(o_path_default, 'wb') as f:
            pickle.dump(s_file_default, f)

    with open(o_path_default, 'rb') as f:
        program_settings.settings_file = pickle.load(f)

    if not os.path.exists(program_settings.settings_file):
        program_settings.settings_file = s_file_default
        program_settings.save()

    program_settings.restore()

    app = QApplication(sys.argv)
    login_controller = LoginPanelController(AuthorizationService())
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
