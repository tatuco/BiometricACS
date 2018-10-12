from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import Qt
from ..Utilities import Observer
from ..UI import Ui_MainWindow
from ..AppStart import program_logs


class MainView(QMainWindow, Observer):

    def __init__(self, in_model, in_controller, parent=None):
        super().__init__(parent=parent, flags=Qt.Window)
        self.parent_o = parent
        self.controller = in_controller
        self.model = in_model
        self.model.add_observer(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionRelogin.triggered.connect(self.controller.relogin_clicked)
        self.ui.actionExit.triggered.connect(self.controller.cancel_clicked)

    def closeEvent(self, *args, **kwargs):
        program_logs.close_log()
        program_logs.save(r'C:\Projects\BiometricACS\BiometricACS\APP\Sources\Logs')
        self.close()

    def model_is_changed(self):
        self.controller.user_changed()