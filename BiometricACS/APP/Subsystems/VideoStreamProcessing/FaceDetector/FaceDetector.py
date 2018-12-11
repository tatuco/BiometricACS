import os
import cv2
import numpy as np
import tensorflow as tf

from .utils import label_map_util
from .utils import visualization_utils_color as vis_util


PATH_TO_CKPT = os.path.join(os.path.dirname(__file__), 'model/frozen_inference_graph_face.pb')
PATH_TO_LABELS = os.path.join(os.path.dirname(__file__), 'protos/face_label_map.pbtxt')
NUM_CLASSES = 2

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


class TensoflowFaceDector(object):

    def __init__(self):

        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        with self.detection_graph.as_default():
            config = tf.ConfigProto()
            config.gpu_options.allow_growth = True
            self.sess = tf.Session(graph=self.detection_graph, config=config)
            self.windowNotSet = True

        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        self.boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        self.scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')

    def run(self, image):
        image_np = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_np_expanded = np.expand_dims(image_np, axis=0)
        (boxes, scores, classes, num_detections) = self.sess.run([self.boxes, self.scores, self.classes, self.num_detections],
            feed_dict={self.image_tensor: image_np_expanded})
        image, max_face, square_coef = vis_util.visualize_boxes_and_labels_on_image_array(
            image,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=1)

        return image, max_face, square_coef
