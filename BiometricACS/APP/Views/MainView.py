import numpy as np
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox, QMenu, QAction, QTreeWidgetItem, QGraphicsScene, QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt5.QtCore import Qt, QRectF, QDate
from PyQt5.QtGui import QImage, QPixmap

from .BaseView import BaseView
from ..Utilities import Observer
from ..UI import Ui_MainWindow
from ..AppStart import program_logs, program_settings
from ..Subsystems import FACE_ALIGNMENT_IMAGE_DESIRED_DIMENSIONS, FACE_LANDMARKS_IMAGE_DESIRED_DIMENSIONS, MAIN_IMAGE_DESIRED_DIMENSIONS
from ...BLL import StatisticsSearchResult


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

        self._previous_date = datetime.now().date()
        self.ui.cmb_department.currentIndexChanged.connect(self.controller.department_change)
        self.ui.btn_clear.clicked.connect(self.controller.clear_statistics_clicked)
        self.ui.wgt_calendar.selectionChanged.connect(self.selected_date_change)
        self.ui.btn_search_statistics.clicked.connect(self.controller.search_statistics_clicked)
        self.ui.btn_save_statistict.clicked.connect(self.controller.save_statistics_clicked)
        attrs = [i for i in dir(StatisticsSearchResult(None, None, None, None, None)) if not i.startswith('_')]
        self.ui.tableStatistics.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableStatistics.setColumnCount(len(attrs))
        self.ui.tableStatistics.setHorizontalHeaderLabels(attrs)
        header = self.ui.tableStatistics.horizontalHeader()
        for i, _ in enumerate(attrs):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        header.setStretchLastSection(True)


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

    def set_statistics_enums(self, departments, checkpoints):
        self.ui.cmb_department.clear()
        self.ui.cmb_department.addItems(departments)
        self.ui.cmb_department.setCurrentIndex(0)
        self.ui.cmb_checkpoint.clear()
        self.ui.cmb_checkpoint.addItems(checkpoints)
        self.ui.cmb_checkpoint.setCurrentIndex(0)

    def set_visit_events(self, events):
        self.ui.cmb_event.clear()
        self.ui.cmb_event.addItems(events)
        self.ui.cmb_event.setCurrentIndex(0)

    def clear_statistics_parameters(self):
        self.ui.cmb_department.setCurrentIndex(0)
        self.ui.cmb_checkpoint.setCurrentIndex(0)
        self.ui.cmb_event.setCurrentIndex(0)
        self.ui.tb_first_name.clear()
        self.ui.tb_last_name.clear()
        self.ui.rbtn_considering_time.setChecked(False)
        self.ui.wgt_calendar.setSelectedDate(datetime.now())
        self.ui.lbl_stop_date.setText(str(datetime.now().date()))
        self.ui.lbl_start_date.setText(str(datetime.now().date()))

    def set_found_visits(self, records, count):
        self.ui.lbl_found_records.setText(str(count))
        if not count:
            self.ui.tableStatistics.clearContents()
            return
        self.ui.tableStatistics.setRowCount(count)
        attrs = [i for i in dir(records[0]) if not i.startswith('_')]
        for i, record in enumerate(records):
            for j, attr in enumerate(attrs):
                self.ui.tableStatistics.setItem(i, j, QTableWidgetItem(str(getattr(record, attr))))

    def selected_date_change(self):
        date = self.ui.wgt_calendar.selectedDate().toPyDate()
        if date == self._previous_date:
            self.ui.lbl_stop_date.setText(str(date))
            self.ui.lbl_start_date.setText(str(date))
        elif date < self._previous_date:
            self.ui.lbl_start_date.setText(str(date))
        else:
            self.ui.lbl_stop_date.setText(str(date))
        self._previous_date = date

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
