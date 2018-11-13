import device
import cv2
import threading

__device__ = []


def device_validator(d):
    return d in __device__


def device_index(d):
    return __device__.index(d) if device_validator(d) else -1


def get_device_list():
    return __device__


class DeviceChecker(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self._available = True

    def stop(self):
        self._available = False

    def run(self):
        global __device__
        while self._available:
            try:
                __device__ = device.getDeviceList()
            except Exception:
                __device__ = []