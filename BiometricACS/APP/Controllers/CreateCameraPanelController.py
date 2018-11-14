from PyQt5.QtWidgets import QMessageBox

from ..Views import CreateCameraPanelView
from ..AppStart import program_logs
from ..Subsystems import device_validator, get_device_list
from ...BLL.DTO import CameraDTO, CamerasVectorDTO, CheckpointDTO


class CreateCameraPanelController:

    def __init__(self, in_model, parent=None):
        self.model = in_model
        self.view = CreateCameraPanelView(in_model, self, parent)

        self.view.set_combobox_items([i.address for i in self.model.checkpoints], [i.value for i in CamerasVectorDTO])

        self.view.show()

    def show_devices_clicked(self):
        devices = ''
        for device in get_device_list():
            if not self.model.is_existing_device(device):
                devices += device + '\n'
        QMessageBox.information(self.view, _('Devices'), _('Unused and currently connected video cameras: \n') + devices)

    def create_clicked(self):
        if self.view.ui.tbDevice == '':
            QMessageBox.warning(self.view, _('Warning'), _('Enter the name or ip of device'))
            return

        device = self.view.ui.tbDevice.text()

        if self.model.is_existing_device(device):
            QMessageBox.warning(self.view, _('Warning'), _('Device already exists'))
            return

        if not device_validator(device):
            QMessageBox.warning(self.view, _('Warning'), _('Device not recognized'))
            return

        camera = CameraDTO()
        camera.vector = list(CamerasVectorDTO)[self.view.ui.cmbVector.currentIndex()]
        camera.device_name = device
        ckpt = self.model.find_checkpoint(self.view.ui.cmbCheckpoint.currentText())
        camera.ckpt_id = ckpt.id
        self.model.add_camera(camera)
        QMessageBox.information(self.view, _('Success'), _('Camera successfully added'))
        self.view.close()
        program_logs.add_camera_log(camera.device_name, camera.vector.value, ckpt.address)
        self.view.parent_o.controller.add_created_camera_item(camera, ckpt.address)
