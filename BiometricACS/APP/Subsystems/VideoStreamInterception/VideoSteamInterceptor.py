import cv2
import time
import threading
import numpy as np

class VideoSteamInterceptor(threading.Thread):

    def __init__(self, video_interceptor, valid_cameras, selected_camera, reindexing_status):
        threading.Thread.__init__(self)
        self.available = True
        self._video_interceptor = video_interceptor
        self._valid_cameras = valid_cameras
        self._selected_camera = selected_camera
        self._reindexing_status = reindexing_status
        
    def check_reindexing(self):
        if self._reindexing_status:
            self. _reindexing_status = False

    def run(self):
        while self.available:
            for camera in self._valid_cameras:
                try:
                    # print(camera.device)
                    capture = camera.capture
                    self.check_reindexing()
                    ret, img = capture.read()
                    selected_camera = self._selected_camera
                    if selected_camera is not None and camera.device == selected_camera.device and camera.vector == selected_camera.vector and camera.ckpt_address == selected_camera.ckpt_address:
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        self._video_interceptor(img)
                except Exception:
                    break



