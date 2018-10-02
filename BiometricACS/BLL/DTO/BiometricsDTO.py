from .BaseDTO import BaseDTO


class BiometricsDTO(BaseDTO):

    @property
    def original_image(self):
        return self._original_image

    @original_image.setter
    def original_image(self, value):
        self._original_image = value

    @property
    def landmarks(self):
        return self._landmarks

    @landmarks.setter
    def landmarks(self, value):
        self._landmarks = value

    @property
    def features(self):
        return self._features

    @features.setter
    def features(self, value):
        self._features = value

    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, value):
        if value > 0:
            self._emp_id = value

    def __init__(self, original_imae=None, landmarks=None, features=None, emp_id=None):
        self._id = None
        self._original_image = original_imae
        self._landmarks = landmarks
        self._features = features
        self._emp_id = emp_id
