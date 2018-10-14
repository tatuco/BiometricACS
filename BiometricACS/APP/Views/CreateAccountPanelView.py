from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget

from .BaseView import BaseView
from ..UI import Ui_wCreateAccountPanel
from ..Utilities import Observer


class CreateAccountPanelView(QDialog, Observer):

    def __init__(self, in_model, in_controller, parent=None):
        super(QWidget, self).__init__(parent)
        self.parent_o = parent
        self.controller = in_controller
        self.model = in_model

        self.ui = Ui_wCreateAccountPanel()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModal)

        BaseView.setup_window_icon(self)

        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnCreate.clicked.connect(self.close)

    def set_combobox_items(self, items):
        self.ui.cmbRole.addItems(items)

    def closeEvent(self, *args, **kwargs):
        self.close()

    def model_is_changed(self):
        pass