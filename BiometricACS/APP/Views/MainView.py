from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox, QMenu, QAction, QTreeWidgetItem
from PyQt5.QtCore import Qt

from .BaseView import BaseView
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

        BaseView.setup_window_icon(self)

        self.ui.treeCameras.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeCameras.customContextMenuRequested.connect(self.open_menu)

        self.ui.actionRelogin.triggered.connect(self.controller.relogin_clicked)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionCreateAccount.triggered.connect(self.controller.create_account_clicked)
        self.ui.actionExport_Accounts.triggered.connect(self.controller.export_accounts_clicked)
        self.ui.actionExportSessionLog.triggered.connect(self.controller.export_session_log_clicked)
        self.ui.actionAddCheckpoint.triggered.connect(self.controller.add_checkpoint_clicked)
        self.ui.actionAddCamera.triggered.connect(self.controller.add_camera_clicked)

    def open_menu(self, position):
        menu = QMenu()
        treeItem = self.ui.treeCameras.itemAt(position)
        if not treeItem:
            add_checkpoint = QAction('Add checkpoint', menu)
            add_checkpoint.triggered.connect(self.controller.add_checkpoint_clicked)
            menu.addAction(add_checkpoint)
        else:
            if treeItem.text(1) == '':
                add_camera = QAction('Add camera', menu)
                add_camera.triggered.connect(self.controller.add_camera_clicked)
                change_address = QAction('Сhange address', menu)
                change_address.triggered.connect(self.controller.change_address_clicked)
                delete_checkpoint = QAction('Delete checkpoint', menu)
                delete_checkpoint.triggered.connect(self.controller.delete_checkpoint_clicled)
                menu.addActions([add_camera, change_address, delete_checkpoint])
            else:
                delete_camera = QAction('Delete camera', menu)
                delete_camera.triggered.connect(self.controller.delete_camera_clicked)
                menu.addAction(delete_camera)
        menu.exec_(self.ui.treeCameras.viewport().mapToGlobal(position))

    def closeEvent(self, *args, **kwargs):
        event = args[0]
        close = QMessageBox().question(self, 'Close', 'You sure?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if close == QMessageBox.Yes:
            program_logs.close_log()
            event.accept()
        else:
            event.ignore()

    def model_is_changed(self):
        self.controller.user_changed()
