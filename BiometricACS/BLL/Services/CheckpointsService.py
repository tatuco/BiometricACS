from .BaseService import BaseService
from ..DTO import CameraDTO, CheckpointDTO, CamerasVectorDTO
from ...DAL import EntitiesUnit, Checkpoint, Camera


class CheckpointService(BaseService):

    @property
    def checkpoints(self):
        return [CheckpointDTO().update(i) for i in self._checkpoint_db.get_all()]

    @property
    def cameras(self):
        return [CameraDTO().update(i) for i in self._camera_db.get_all()]

    def find_checkpoint(self, address):
        ckpt = self._checkpoint_db.find([Checkpoint.address == address])
        if not ckpt:
            return None
        return CheckpointDTO().update(ckpt[0])

    def checkpoint_is_exist(self, address):
        return self._checkpoint_db.find([Checkpoint.address == address]) != []

    def add_checkpoint(self, address):
        self._checkpoint_db.create(CheckpointDTO(address))
        self._db.save()

    def add_camera(self, camera):
        self._camera_db.create(camera)
        self._db.save()

    def edit_checkpoint(self, old_address, new_address):
        ckpt = self._checkpoint_db.find([Checkpoint.address == old_address])[0]
        ckpt.address = new_address
        self._db.save()

    def delete_camera(self, camera):
        cam = self._camera_db.find([Camera.vector == camera.vector, Camera.device_name == camera.device_name, Camera.ckpt_id == camera.ckpt_id])[0]
        self._camera_db.delete(cam)
        self._db.save()

    def delete_checkpoint(self, checkpoint):
        ckpt = self._checkpoint_db.find([Checkpoint.address == checkpoint.address])[0]
        self._checkpoint_db.delete(ckpt)
        self._db.save()

    def is_existing_device(self, device_name):
        cameras = self._camera_db.find([Camera.device_name == device_name])
        return True if cameras else False

    def count_of_cameras(self, ckpt_id):
        return len(self._camera_db.find([Camera.ckpt_id == ckpt_id]))

    def __init__(self, connection_string):
        self._db = EntitiesUnit(connection_string)
        self._camera_db = self._db.camera_repository
        self._checkpoint_db = self._db.checkpoint_repository
        self.selected_address = None
