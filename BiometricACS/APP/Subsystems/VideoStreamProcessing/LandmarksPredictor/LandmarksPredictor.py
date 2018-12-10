import cv2
import dlib
import numpy as np
import os

from ..FaceInformation import FACIAL_LANDMARKS_68_IDXS


class LandmarksPredictor:

    def __init__(self, ):
        self._predictor = dlib.shape_predictor(os.path.abspath(".\APP\Subsystems\VideoStreamProcessing\LandmarksPredictor\Model\shape_predictor_68_face_landmarks.dat"))

    def run(self, image):
        image = np.copy(image)
        obj_d = self._predictor(image, dlib.rectangle(0, 0, image.shape[0], image.shape[1]))
        points = [*range(*FACIAL_LANDMARKS_68_IDXS['mouth']), *range(*FACIAL_LANDMARKS_68_IDXS['right_eye']), *range(*FACIAL_LANDMARKS_68_IDXS['left_eye'])]
        for i in points:
            point = obj_d.part(i)
            cv2.circle(image, (point.x, point.y), 2, (255, 0, 0), -1)
        return image, obj_d
