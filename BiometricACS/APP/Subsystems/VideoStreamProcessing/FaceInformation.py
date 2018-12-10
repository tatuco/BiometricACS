import numpy as np
from collections import OrderedDict

MAIN_IMAGE_DESIRED_DIMENSIONS = [480, 640, 3]
FACE_LANDMARKS_IMAGE_DESIRED_DIMENSIONS = [180, 180, 3]
FACE_ALIGNMENT_IMAGE_DESIRED_DIMENSIONS = [180, 180, 3]

FACIAL_LANDMARKS_68_IDXS = OrderedDict([
    ("mouth", (48, 68)),
    ("right_eyebrow", (17, 22)),
    ("left_eyebrow", (22, 27)),
    ("right_eye", (36, 42)),
    ("left_eye", (42, 48)),
    ("nose", (27, 36)),
    ("jaw", (0, 17))
])


def shape_to_np(shape, dtype=np.int):
    coords = np.zeros((shape.num_parts, 2), dtype=dtype)
    for i in range(0, shape.num_parts):
        coords[i] = (shape.part(i).x, shape.part(i).y)
    return coords
