from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox, QMenu, QAction, QTreeWidgetItem, QGraphicsScene
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QImage, QPixmap
import numpy as np

from .BaseView import BaseView
from ..Utilities import Observer
from ..UI import Ui_MainWindow
from ..AppStart import program_logs, program_settings
from ..Subsystems import FACE_ALIGNMENT_IMAGE_DESIRED_DIMENSIONS, FACE_LANDMARKS_IMAGE_DESIRED_DIMENSIONS, MAIN_IMAGE_DESIRED_DIMENSIONS


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
        self.ui.treeCameras.itemClicked.connect(self.controller.selected_item_change)

        self.ui.actionRelogin.triggered.connect(self.controller.relogin_clicked)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionCreateAccount.triggered.connect(self.controller.create_account_clicked)
        self.ui.actionExport_Accounts.triggered.connect(self.controller.export_accounts_clicked)
        self.ui.actionExportSessionLog.triggered.connect(self.controller.export_session_log_clicked)
        self.ui.actionAddCheckpoint.triggered.connect(self.controller.add_checkpoint_clicked)
        self.ui.actionAddCamera.triggered.connect(self.controller.add_camera_clicked)
        self.ui.actionOpenSettings.triggered.connect(self.controller.open_settings_panel_clicked)
        self.ui.actionExportSettings.triggered.connect(self.controller.export_settings_clicked)

    def open_menu(self, position):
        if not self.controller.user_is_technical_engineer:
            return
        menu = QMenu()
        treeItem = self.ui.treeCameras.itemAt(position)
        if not treeItem:
            add_checkpoint = QAction(_('Add checkpoint'), menu)
            add_checkpoint.triggered.connect(self.controller.add_checkpoint_clicked)
            menu.addAction(add_checkpoint)
        else:
            if treeItem.text(1) == '':
                add_camera = QAction(_('Add camera'), menu)
                add_camera.triggered.connect(self.controller.add_camera_clicked)
                change_address = QAction(_('Сhange address'), menu)
                change_address.triggered.connect(self.controller.change_address_clicked)
                delete_checkpoint = QAction(_('Delete checkpoint'), menu)
                delete_checkpoint.triggered.connect(self.controller.delete_checkpoint_clicked)
                menu.addActions([add_camera, change_address, delete_checkpoint])
            else:
                delete_camera = QAction(_('Delete camera'), menu)
                delete_camera.triggered.connect(self.controller.delete_camera_clicked)
                menu.addAction(delete_camera)
        menu.exec_(self.ui.treeCameras.viewport().mapToGlobal(position))

    def set_face_detection_image(self, image):
        if not list(image):
            self.set_default_images(MAIN_IMAGE_DESIRED_DIMENSIONS, f=self.set_face_detection_image)
            return
        pixMap = self.image_to_pixmap(image)
        self.ui.gvFaceDetection.setPixmap(pixMap)

    def set_landmarks_face_image(self, image):
        if not list(image):
            self.set_default_images(FACE_LANDMARKS_IMAGE_DESIRED_DIMENSIONS, f=self.set_landmarks_face_image)
            return
        pixMap = self.image_to_pixmap(image)
        self.ui.gvLandmarksDetection.setPixmap(pixMap)

    def set_alignment_face_image(self, image):
        if not list(image):
            self.set_default_images(FACE_ALIGNMENT_IMAGE_DESIRED_DIMENSIONS, f=self.set_alignment_face_image)
            return
        pixMap = self.image_to_pixmap(image)
        self.ui.gvFaceNormalization.setPixmap(pixMap)

    def image_to_pixmap(self, image):
        image = np.array(image.data).astype(np.uint8)
        imgQ = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        imgQ = imgQ.scaled(image.shape[1], image.shape[0], Qt.KeepAspectRatioByExpanding)
        pixMap = QPixmap.fromImage(imgQ)
        return pixMap

    def set_default_images(self, size, f):
        image = np.full(size, 255, dtype=np.int32)
        f(image)

    def closeEvent(self, *args, **kwargs):
        event = args[0]
        close = QMessageBox().question(self, _('Close'), _('You sure?'), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if close == QMessageBox.Yes:
            program_logs.close_log()
            event.accept()
            self.controller.exit()
        else:
            event.ignore()

    def model_is_changed(self):
        self.controller.user_changed()
