from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget

from .BaseView import BaseView
from ..UI import Ui_WindowSettingsPanel
from ..Utilities import Observer


class SettingsPanelView(QDialog, Observer):

    def __init__(self, in_model, in_controller, parent=None):
        super(QWidget, self).__init__(parent)
        self.parent_o = parent
        self.controller = in_controller
        self.model = in_model

        self.ui = Ui_WindowSettingsPanel()
        self.ui.setupUi(self)
        self.setWindowModality(Qt.WindowModal)

        BaseView.setup_window_icon(self)

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_apply.clicked.connect(self.controller.apply_clicked)
        self.ui.btn_browse_backup.clicked.connect(self.controller.browse_backup_clicked)
        self.ui.btn_browse_logs.clicked.connect(self.controller.browse_logs_clicked)
        self.ui.btn_browse_settings.clicked.connect(self.controller.browse_settings_clicked)

    def set_cmb_language_items(self,items, selected_item):
        self.ui.cmb_language.addItems(items)
        self.ui.cmb_language.setCurrentIndex(items.index(selected_item))

    def set_cmb_log_saving_items(self, items, selected_item):
        self.ui.cmb_log_saving.addItems(items)
        self.ui.cmb_language.setCurrentIndex(items.index(selected_item))

    def set_labels_value(self, settings):
        self.ui.lbl_setting_path.setText(settings.settings_file)
        self.ui.lbl_logs_path.setText(settings.logs_path)
        self.ui.lbl_backup_path.setText(settings.backup_path)
        self.ui.tb_conn_str.setText(settings.connection_string)
        self.ui.tb_square_coeff.setText(str(settings.square_coef))
        self.ui.tb_truth_factor.setText(str(settings.truth_factor))

    def closeEvent(self, *args, **kwargs):
        self.close()

    def model_is_changed(self):
        pass
