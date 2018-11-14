from PyQt5.QtWidgets import QListWidgetItem, QMessageBox, QTreeWidgetItem, QInputDialog
from PyQt5.QtCore import Qt

from ..Views import MainView, ReloginPanelView, FileDialogView
from ..AppStart import program_logs, program_settings
from ..Subsystems import CameraModel, MainLoop
from ..Controllers.ReloginPanelController import ReloginPanelController
from ..Controllers.CreateAccountPanelController import CreateAccountPanelController
from ..Controllers.CreateCameraPanelController import CreateCameraPanelController
from ...BLL import AuthorizationService
from ...BLL.DTO import AccountDTO, AccountRoleDTO, CheckpointDTO, VisitDTO, CamerasVectorDTO, EmployeeStatusDTO, CameraDTO


class MainController:

    def __init__(self, in_model, parent=None):
        self.model = in_model
        self.view = MainView(in_model, self, parent)

        self.user_is_technical_engineer = None
        self.user_changed()

        program_logs.reset_handler(self.add_session_log)

        video_cameras = self.initialize_checkpoints()
        face_detection_interceptor = self.view.set_face_detection_image
        self.MainLoopVideoStream = MainLoop(video_cameras, program_logs, program_settings, face_detection_interceptor, None, None, None)
        self.view.set_default_images()

        self.view.show()

    def _update_ui_role(self, is_technical_engineer):
        self.view.ui.menuData.setEnabled(is_technical_engineer)
        self.view.ui.menuSettings.setEnabled(is_technical_engineer)
        self.view.ui.actionCreateAccount.setEnabled(is_technical_engineer)
        self.view.ui.actionExport_Accounts.setEnabled(is_technical_engineer)
        self.view.ui.menuCheckpoints.setEnabled(is_technical_engineer)

    def user_changed(self):
        if self.model.relogin_service.user.role == AccountRoleDTO.viewer:
            self.user_is_technical_engineer = False
            self._update_ui_role(self.user_is_technical_engineer)
        elif self.model.relogin_service.user.role == AccountRoleDTO.technical_engineer:
            self.user_is_technical_engineer = True
            self._update_ui_role(self.user_is_technical_engineer)

    def relogin_clicked(self):
        self.model.relogin_service = AuthorizationService(program_settings.connection_string, self.model.relogin_service.user)
        ReloginPanelController(self.model.relogin_service, self.view)

    def create_account_clicked(self):
        CreateAccountPanelController(self.model.accounts_service, self.view)

    def export_accounts_clicked(self):
        file_name = FileDialogView.save_any_file_dialog(self.view)
        if file_name == '':
            return
        with open(file_name, 'w') as f:
            for acc in self.model.accounts_service.accounts:
                f.write(str(acc) + '\n')
        QMessageBox.information(self.view, _('Success'), _('Accounts successfully exported'))
        program_logs.export_accounts(file_name)

    def export_session_log_clicked(self):
        file_name = FileDialogView.save_log_file_dialog(self.view)
        if file_name == '':
            return
        with open(file_name, 'w') as f:
            for log in program_logs.logs:
                f.write(str(log) + '\n')
            QMessageBox.information(self.view, _('Success'), _('Session log successfully exported'))
            program_logs.export_logs_log(file_name)

    def add_session_log(self, log):
        try:
            if len(log) > 0:
                for i, l in enumerate(log):
                    item = QListWidgetItem(str(l))
                    item.setForeground(l.level.value)
                    self.view.ui.lvVisitsLog.addItem(item)
                self.view.ui.statusbarCurrentEvent.showMessage(log[len(log) - 1].event)
        except TypeError:
            item = QListWidgetItem(str(log))
            item.setForeground(log.level.value)
            self.view.ui.lvVisitsLog.addItem(item)
            self.view.ui.statusbarCurrentEvent.showMessage(log.event)

    def create_checkpoint_item(self, address):
        top_item = QTreeWidgetItem()
        top_item.setText(0, address)
        top_item.setFlags(top_item.flags() | Qt.ItemIsDragEnabled)
        return top_item

    def create_camera_item(self, camera):
        child = QTreeWidgetItem([camera.device_name, camera.vector.value])
        child.setFlags(child.flags() | Qt.ItemNeverHasChildren)
        return child

    def initialize_checkpoints(self):
        self.view.ui.treeCameras.setHeaderLabels(['Device', 'Vector'])

        cameras = []

        for checkpoint in self.model.checkpoints_service.checkpoints:
            top_item = self.create_checkpoint_item(checkpoint.address)
            for camera in self.model.checkpoints_service.cameras:
                if camera.ckpt_id == checkpoint.id:
                    cameras.append(CameraModel(camera.device_name, camera.vector, checkpoint.address))
                    child = self.create_camera_item(camera)
                    top_item.addChild(child)
            self.view.ui.treeCameras.addTopLevelItem(top_item)
        self.view.ui.treeCameras.resizeColumnToContents(0)

        return cameras

    def add_checkpoint_clicked(self):
        text, ok = QInputDialog().getText(self.view, _('Checkpoint'), _('Enter the address of the checkpoint:'))
        if ok:
            if text != '':
                if self.model.checkpoints_service.checkpoint_is_exist(text):
                    QMessageBox.warning(self.view, _('Warning'), _('Сheckpoint already exists'))
                else:
                    self.model.checkpoints_service.add_checkpoint(text)
                    self.view.ui.treeCameras.addTopLevelItem(self.create_checkpoint_item(text))
                    program_logs.add_checkpoint_log(text)
                    QMessageBox.information(self.view, _('Success'), _('Сheckpoint successfully added'))
            else:
                QMessageBox.warning(self.view, _('Warning'), _('Enter address'))

    def add_camera_clicked(self):
        selected_checkpoint = self.view.ui.treeCameras.selectedItems()
        selected_checkpoint = selected_checkpoint[0].text(0) if selected_checkpoint else None
        if selected_checkpoint:
            self.model.checkpoints_service.selected_address = selected_checkpoint
        CreateCameraPanelController(self.model.checkpoints_service, self.view)

    def change_address_clicked(self):
        selected_item = self.view.ui.treeCameras.selectedItems()[0]
        old_address = selected_item.text(0)
        text, ok = QInputDialog().getText(self.view, _('Checkpoint'), _('Enter the address of the checkpoint:'), text=old_address)
        if ok:
            if text != '':
                if self.model.checkpoints_service.checkpoint_is_exist(text):
                    QMessageBox.warning(self.view, _('Warning'), _('Сheckpoint already exists'))
                else:
                    self.model.checkpoints_service.edit_checkpoint(old_address, text)
                    selected_item.setText(0, text)
                    program_logs.change_checkpoint_address_log(old_address, text)
                    QMessageBox.information(self.view, _('Success'), _('Сheckpoint successfully changed'))
            else:
                QMessageBox.warning(self.view, _('Warning'), _('Enter address'))

    def delete_camera_clicked(self):
        remove = QMessageBox().question(self.view, _('Camera'), _('Do you really want to remove the camera?'), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if remove == QMessageBox.No:
            return
        selected_item = self.view.ui.treeCameras.selectedItems()[0]
        ckpt = selected_item.parent()
        address = ckpt.text(0)
        camera = CameraDTO()
        camera.ckpt_id = self.model.checkpoints_service.find_checkpoint(address).id
        camera.vector = list(CamerasVectorDTO)[[i.value for i in list(CamerasVectorDTO)].index(selected_item.text(1))]
        camera.device_name = selected_item.text(0)

        self.model.checkpoints_service.delete_camera(camera)
        self.MainLoopVideoStream.remove_camera(CameraModel(camera.device_name, camera.vector, address))
        self.remove_selected_item()

        program_logs.delete_camera_log(camera.device_name, camera.vector.value, address)
        QMessageBox.information(self.view, _('Success'), _('Camera removed successfully'))

    def delete_checkpoint_clicled(self):
        ckpt = self.model.checkpoints_service.find_checkpoint(self.view.ui.treeCameras.selectedItems()[0].text(0))
        if self.model.checkpoints_service.count_of_cameras(ckpt.id) != 0:
            QMessageBox.warning(self.view, _('Warning'), _('At the selected checkpoint there are still cameras'))
            return

        remove = QMessageBox().question(self.view, _('Camera'), _('Do you really want to remove the checkpoint?'), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if remove == QMessageBox.No:
            return

        self.model.checkpoints_service.delete_checkpoint(ckpt)
        self.remove_selected_item()
        program_logs.delete_checkpoint_log(ckpt.address)
        QMessageBox.information(self.view, _('Success'), _('Checkpoint removed successfully'))

    def remove_selected_item(self):
        root = self.view.ui.treeCameras.invisibleRootItem()
        for item in self.view.ui.treeCameras.selectedItems():
            (item.parent() or root).removeChild(item)

    def add_created_camera_item(self, camera, ckpt_address):
        ckpt_item = self.view.ui.treeCameras.findItems(ckpt_address, Qt.MatchFixedString)[0]
        camera_item = self.create_camera_item(camera)
        ckpt_item.addChild(camera_item)
        self.MainLoopVideoStream.add_camera(CameraModel(camera.device_name, camera.vector, ckpt_address))

    def selected_item_change(self):
        selected_item = self.view.ui.treeCameras.selectedItems()[0]
        if selected_item.text(1) == '':
            self.MainLoopVideoStream.set_selected_camera(None)
            self.view.set_default_images()
            self.view.set_default_images()
            return
        ckpt = selected_item.parent()
        address = ckpt.text(0)
        camera = CameraDTO()
        camera.vector = list(CamerasVectorDTO)[[i.value for i in list(CamerasVectorDTO)].index(selected_item.text(1))]
        camera.device_name = selected_item.text(0)
        self.MainLoopVideoStream.set_selected_camera(CameraModel(camera.device_name, camera.vector, address))

    def exit(self):
        self.MainLoopVideoStream.stop()
