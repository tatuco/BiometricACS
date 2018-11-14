from PyQt5.QtWidgets import QFileDialog


class FileDialogView:

    @staticmethod
    def _save_file_dialog(filters, parent):
        dialog = QFileDialog()
        options = dialog.options()
        options |= dialog.DontUseCustomDirectoryIcons
        file_name, _ = dialog.getSaveFileName(parent, _("Save"), '', filters, options=options )
        return file_name

    @staticmethod
    def save_log_file_dialog(parent):
        return FileDialogView._save_file_dialog(_("Log files (*.log )"), parent)

    @staticmethod
    def save_any_file_dialog(parent):
        return FileDialogView._save_file_dialog(_("All Files (*)"), parent)

