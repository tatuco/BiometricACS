from PyQt5.QtWidgets import QMessageBox
import cv2

from ..Views import CreateCameraPanelView
from ..AppStart import program_logs
from ...BLL.DTO import CameraDTO, CamerasVectorDTO, CheckpointDTO


class CreateCameraPanelController:

    def __init__(self, in_model, parent=None):
        self.model = in_model
        self.view = CreateCameraPanelView(in_model, self, parent)

        self.view.set_combobox_items([i.address for i in self.model.checkpoints], [i.value for i in CamerasVectorDTO])

        self.view.show()

    def create_clicked(self):
        if self.view.ui.tbDevice == '':
            QMessageBox.warning(self.view, 'Warning', 'Enter the name or ip of device ')
            return
        try:
            device = self.view.ui.tbDevice.text()
            #TODO device = Приведение к устройству
            # if device.isdigit():
            #     device = int(device)

            capture = cv2.VideoCapture(int(device))
            ret, frame = capture.read()
            if not ret:
                raise Exception()
                
        except Exception:
            QMessageBox.warning(self.view, 'Warning', 'Device not recognized')
            return

        camera = CameraDTO()
        camera.vector = list(CamerasVectorDTO)[self.view.ui.cmbVector.currentIndex()]
        camera.device_name = device
        ckpt = self.model.find_checkpoint(self.view.ui.cmbCheckpoint.currentText())
        camera.ckpt_id = ckpt.id
        self.model.add_camera(camera)
        QMessageBox.information(self.view, 'Success', 'Camera successfully added')
        self.view.close()
        program_logs.add_camera_log(camera.device_name, camera.vector.value, ckpt.address)
        self.view.parent_o.controller.add_created_camera_item(camera, ckpt.address)