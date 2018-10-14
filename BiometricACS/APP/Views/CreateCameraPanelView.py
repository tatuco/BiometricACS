from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDialog

from .BaseView import BaseView
from ..Utilities import Observer
from ..UI import Ui_wCreateCameraPanel


class CreateCameraPanelView(QDialog, Observer):

    def __init__(self, in_model, in_controller, parent=None):
        super(QWidget, self).__init__(parent)
        self.parent_o = parent
        self.controller = in_controller
        self.model = in_model

        self.ui = Ui_wCreateCameraPanel()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModal)

        BaseView.setup_window_icon(self)

        self.ui.btnCancel.clicked.connect(self.close)
        self.ui.btnCreate.clicked.connect(self.controller.create_clicked)

    def set_combobox_items(self, checkpoints, vectors):
        self.ui.cmbCheckpoint.addItems(checkpoints)
        if self.model.selected_address:
            self.ui.cmbCheckpoint.setCurrentIndex(checkpoints.index(self.model.selected_address))
            self.model.selected_address=None
        self.ui.cmbVector.addItems(vectors)

    def model_is_changed(self):
        pass

