import threading
import cv2
import numpy as np
from multiprocessing import Process
from threading import Thread
from queue import Queue, Empty

from .VideoStreamInterception import device_validator
from .VideoStreamInterception.DeviceValidator import DeviceChecker, device_index
from .VideoStreamInterception.VideoSteamInterceptor import VideoSteamInterceptor
from .VideoStreamProcessing import TensoflowFaceDector, LandmarksPredictor, FaceAligner
from .VideoStreamProcessing import FACE_LANDMARKS_IMAGE_DESIRED_DIMENSIONS


class VideoStream(Thread):

    def __init__(self, q_selected, q_lock, logger,
                 camera, device_index_getter,
                 settings, biometrics_eq,
                 image_faces_interceptor, image_landmarks_interceptor, image_alignment_interceptor,
                 employee_interceptor,
                 face_detector, landmarks_detector, face_alignmenter, biometrics_detector):
        Thread.__init__(self)

        self._available = True

        self._q_selected = q_selected
        self._q_lock = q_lock
        self._logger = logger

        self._camera = camera
        self._is_locked = False

        self._is_selected = False
        self._device_index_getter = device_index_getter
        self._index = None
        self._capture = None
        self._settings = settings
        self._biometrics_eq = biometrics_eq

        self._image = []
        self._image_faces = []
        self._image_landmarks = []
        self._image_alignment = []

        self._face_detector = face_detector
        self._landmarks_predictor = landmarks_detector
        self._face_alignmenter = face_alignmenter
        self._biometrics_detector = biometrics_detector

        self._image_faces_interceptor = image_faces_interceptor
        self._image_landmarks_interceptor = image_landmarks_interceptor
        self._image_alignment_interceptor = image_alignment_interceptor

        self._employee_interceptor = employee_interceptor

    def stop(self):
        self._available = False

    def index_checker(self):
        ind = self._device_index_getter(self._camera.device)
        if ind != self._index:
            if ind == -1:
                self._logger.camera_turned_off_log(self._camera.ckpt_address, self._camera.device)
                if self._capture:
                    self._capture.release()
                self._capture = None
            if ind >= 0 and self._index is not None and self._index >= 0:
                return
            if ind >= 0 and (self._index is None or self._index == -1):
                self._logger.camera_turned_on_log(self._camera.ckpt_address, self._camera.device)
                self._capture = cv2.VideoCapture(ind)
            self._index = ind

    def selected_checker(self):
        if not self._q_selected.empty():
            status = self._q_selected.get(False)
            self._is_selected = bool(status)
            self._q_selected.task_done()

    def lock_checker(self):
        if not self._q_lock.empty():
            status = self._q_lock.get(False)
            self._is_locked = bool(status)
            self._q_lock.task_done()

    def run(self):
        face_desired_height = FACE_LANDMARKS_IMAGE_DESIRED_DIMENSIONS[0]
        while self._available:

            self.index_checker()
            self.selected_checker()
            if self._index == -1:
                if self._is_selected:
                    self._image_faces_interceptor([])
                    self._image_landmarks_interceptor([])
                    self._image_alignment_interceptor([])
                continue

            try:
                ret, self._image = self._capture.read()
            except Exception:
                continue

            if not ret:
                old_ind = self._index
                self.index_checker()
                if old_ind == self._index:
                    self._capture.release()
                    self._capture = None
                    self._index = -1
                    self.index_checker()
                continue

            self._image_faces, face, square_coef = self._face_detector.run(self._image)
            if self._is_selected:
                self._image_faces_interceptor(cv2.cvtColor(self._image_faces, cv2.COLOR_BGR2RGB))

            if square_coef==0:
                continue

            if square_coef < self._settings.square_coef:
                self._image_landmarks_interceptor([])
                self._image_alignment_interceptor([])
                continue

            self._image_landmarks, landmarks = self._landmarks_predictor.run(face)
            thumbnail_image_shape = face_desired_height, int(face_desired_height / face.shape[1] * face.shape[0])
            if self._is_selected:
                thumbnail_image_landmarks = cv2.resize(self._image_landmarks, thumbnail_image_shape, interpolation=cv2.INTER_LINEAR)
                self._image_landmarks_interceptor(thumbnail_image_landmarks)

            self._image_alignment = self._face_alignmenter.run(face, landmarks)
            if self._is_selected:
                thumbnail_image_alignment = cv2.resize(self._image_alignment, thumbnail_image_shape, interpolation=cv2.INTER_LINEAR)
                self._image_alignment_interceptor(thumbnail_image_alignment)


            # self.lock_checker()
            # if self._is_locked:
            #     continue
            #
            # biometrics = self._biometrics_detector(self._image_alignment)
            # eq_result, employee = self._biometrics_eq(biometrics)
            # if eq_result < self._trust_factor:
            #     continue
            #
            # if self._is_selected:
            #     self._employee_interceptor('%s %s' % (employee.first_name, employee.last_name))
            #
            # if employee.status.value != 'working':
            #     continue
            #
            # self._logger.visit_log(employee.first_name, employee.last_name, self._camera.ckpt_address)
            # # TODO заморозка прохода конкретного человека


class MainLoop:

    def stop(self):
        for process in self._processes:
            process.stop()
        self._device_checker.stop()
        self._processes = []
        self._q_lock = []
        self._q_selected = []
        self._selected_camera = None

    def add_camera(self, camera):
        self._cameras.append(camera)
        self._create_process(camera)

    def remove_camera(self, camera):
        ind = self._find_camera_index(camera.device)
        self._processes[ind].stop()
        del self._cameras[ind]
        del self._processes[ind]
        del self._q_lock[ind]
        del self._q_selected[ind]

    def set_selected_camera(self, camera):
        if self._selected_camera:
            for i, q in enumerate(self._q_selected):
                q.put(False)
        if camera:
            new_ind = self._find_camera_index(camera.device)
            self._q_selected[new_ind].put(True)
            self._selected_camera = self._cameras[new_ind]
        else:
            self._selected_camera = None

    def lock_camera(self, camera):
        ind = self._find_camera_index(camera.device)
        self._q_lock[ind].put(True)

    def unlock_camera(self, camera):
        ind = self._find_camera_index(camera.device)
        self._q_lock[ind].put(False)

    def _find_camera_index(self, device):
        for i, camera in enumerate(self._cameras):
            if camera.device == device:
                return i

    def _create_process(self, camera):
        q_selected = Queue(1)
        q_lock = Queue(1)

        self._q_selected.append(q_selected)
        self._q_lock.append(q_lock)

        face_detector = self._face_detector
        landmarks_detector = self._landmarks_predictor
        face_alignmenter = FaceAligner()
        biometrics_detector = None

        proc = VideoStream(q_selected, q_lock, self._program_logs, camera,
                           device_index, self._settings, self._biometrics_eq,
                           self._faces_interceptor, self._landmarks_interceptor,
                           self._aligment_interceptor, self._employee_interceptor,
                           face_detector, landmarks_detector, face_alignmenter, biometrics_detector)
        self._processes.append(proc)
        proc.start()

    def __init__(self, cameras, program_logs, program_setting, faces_interceptor, landmarks_interceptor, aligment_interceptor, employee_interceptor):
        self._cameras = cameras
        self._selected_camera = None
        self._processes = []
        self._q_selected = []
        self._q_lock = []

        self._program_logs = program_logs
        self._settings = program_setting
        self._biometrics_eq = None

        self._faces_interceptor = faces_interceptor
        self._landmarks_interceptor = landmarks_interceptor
        self._aligment_interceptor = aligment_interceptor
        self._employee_interceptor = employee_interceptor

        self._face_detector = TensoflowFaceDector()
        self._landmarks_predictor = LandmarksPredictor()

        self._device_checker = DeviceChecker()
        self._device_checker.start()

        for camera in cameras:
            self._create_process(camera)
