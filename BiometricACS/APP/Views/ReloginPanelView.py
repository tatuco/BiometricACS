from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5 import QtCore
from ..Utilities import Observer
from ..UI import Ui_wLoginPanel


class ReloginPanelView(QDialog, Observer):
    def __init__(self, in_model, in_controller, parent=None):
        super(QWidget, self).__init__(parent)
        self.parent_o = parent
        self.controller = in_controller
        self.model = in_model
        self.model.add_observer(self)

        self.ui = Ui_wLoginPanel()
        self.ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModal)

        self.ui.btnLogin.clicked.connect(self.controller.login_clicked)
        self.ui.btnCancel.clicked.connect(self.controller.cancel_clicked)

    def keyPressEvent(self, QKeyEvent):
        self.controller.enter_clicked(QKeyEvent)

    def closeEvent(self, *args, **kwargs):
        self.close()

    def model_is_changed(self):
        self.controller.relogin()