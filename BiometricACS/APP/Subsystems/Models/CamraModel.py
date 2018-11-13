import cv2
import multiprocessing
import queue


class CameraModel:

    def __init__(self, device=None, vector=None, ckpt_address=None):
        self.device = device
        self.vector = vector
        self.ckpt_address = ckpt_address
