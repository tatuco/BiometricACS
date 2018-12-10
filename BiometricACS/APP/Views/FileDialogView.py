from PyQt5.QtWidgets import QFileDialog


class FileDialogView:

    @staticmethod
    def _save_file_dialog(filters, parent, base_directory):
        dialog = QFileDialog()
        options = dialog.options()
        options |= dialog.DontUseCustomDirectoryIcons
        file_name, res = dialog.getSaveFileName(parent, _('Save'), base_directory, filters, options=options)
        return file_name

    @staticmethod
    def save_log_file_dialog(parent, base_directory=''):
        return FileDialogView._save_file_dialog(_("Log files (*.log )"), parent, base_directory)

    @staticmethod
    def save_any_file_dialog(parent, base_directory=''):
        return FileDialogView._save_file_dialog(_("All Files (*)"), parent, base_directory)

    @staticmethod
    def save_settings_file_dialog(parent, base_directory=''):
        return FileDialogView._save_file_dialog(_("Settings file (*.set)"), parent, base_directory)

    @staticmethod
    def open_any_directory_dialog(parent, base_directory=''):
        dialog = QFileDialog(parent)
        options = dialog.options()
        options |= dialog.DontUseCustomDirectoryIcons
        dir_name = dialog.getExistingDirectory(parent, _('Directory selection'), base_directory, options)
        return dir_name

    @staticmethod
    def open_settings_file_dialog(parent, base_path=''):
        dialog = QFileDialog(parent)
        options = dialog.options()
        options |= dialog.DontUseCustomDirectoryIcons
        file_name,res = dialog.getOpenFileName(parent, _('File selection'), base_path, _("Settings file (*.set)"))
        return file_name, res