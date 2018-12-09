import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QCloseEvent

from ..Views import SettingsPanelView, FileDialogView
from ..AppStart import program_logs, program_settings
from ...BLL import SettingsDTO


class SettingsPanelController:

    def __init__(self, in_model, parent=None):
        self.model = in_model
        self.parent_o = parent
        self.view = SettingsPanelView(in_model, self, parent)

        self.view.set_cmb_log_saving_items([str(True), str(False)], str(program_settings.logs_saving))
        self.view.set_cmb_language_items(self.model.get_locales(), program_settings.language)
        self.view.set_labels_value(program_settings)

        self.view.show()

    def apply_clicked(self):

        square_coef_text = self.view.ui.tb_square_coeff.text()
        truth_factor_text = self.view.ui.tb_truth_factor.text()
        self.model.settings.language=self.view.ui.cmb_language.currentText()
        self.model.settings.logs_saving = bool(self.view.ui.cmb_log_saving.currentText())
        self.model.settings.connection_string = self.view.ui.tb_conn_str.text()

        try:
            self.model.settings.square_coef = float(square_coef_text)
        except ValueError:
            self.model.settings.square_coef = 0
        try:
            self.model.settings.truth_factor = float(truth_factor_text)
        except ValueError:
            self.model.settings.square_coef = 0

        if not self.model.is_valid_values():
            QMessageBox.warning(self.view, _('Warning'), _('Incorrect truth factor or square coefficient values entered.\nValues can range from 0 to 1'))
            return
        if not self.model.is_valid_paths():
            QMessageBox.warning(self.view, _('Warning'), _('Incorrect paths to files or directories entered'))
            return
        if not self.model.is_valid_conn_str():
            QMessageBox.warning(self.view, _('Warning'), _('Database doesnt exists or username/password incorrect'))
            return

        if self.model.settings.settings_file != program_settings.settings_file or self.model.settings.language != program_settings.language or \
                self.model.settings.connection_string != program_settings.connection_string:
            close = QMessageBox().question(self.view, _('Restart'), _('To apply the selected settings will require a restart.\nRestart the system?'),
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if close == QMessageBox.Yes:
                self.parent_o.controller.exit()

                if self.model.settings.settings_file != program_settings.settings_file:
                    if not program_settings.forced_restore(self.model.settings.settings_file, program_settings.settings_file):
                        QMessageBox.warning(self.view, _('Warning'), _('Settings file is damaged!\nSettings returned to their previous state.')+_('\nRestart canceled.'))
                        self.view.close()
                        return

                program_settings.update_obj(self.model.settings)
                program_settings.save()
                program_logs.change_settings_log()
                program_logs.restart_log()
                self.view.close()
                self.parent_o.destroy()
                do_restart()
                return
            else:
                return

        program_settings.update_obj(self.model.settings)
        program_settings.save()
        program_logs.change_settings_log()
        QMessageBox.information(self.view, _('Success'), _('Settings successfully applied'))
        self.view.close()

    def browse_backup_clicked(self):
        backup_directory = FileDialogView.open_any_directory_dialog(self.view, self.model.settings.backup_path)
        if backup_directory:
            self.model.settings.backup_path = os.path.abspath(backup_directory)
            self.view.ui.lbl_backup_path.setText(backup_directory)

    def browse_logs_clicked(self):
        logs_directory = FileDialogView.open_any_directory_dialog(self.view, self.model.settings.logs_path)
        if logs_directory:
            self.model.settings.logs_path = os.path.abspath(logs_directory)
            self.view.ui.lbl_logs_path.setText(logs_directory)

    def browse_settings_clicked(self):
        settings_file, res = FileDialogView.open_settings_file_dialog(self.view, self.model.settings.settings_file)
        settings_file = os.path.abspath(settings_file)
        if not os.path.isdir(settings_file):
            self.model.settings.settings_file = os.path.abspath(settings_file)
            self.view.ui.lbl_setting_path.setText(settings_file)
