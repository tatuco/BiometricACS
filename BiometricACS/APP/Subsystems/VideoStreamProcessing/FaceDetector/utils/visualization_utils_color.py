import collections
import cv2
import numpy as np
import tensorflow as tf


def visualize_boxes_and_labels_on_image_array(image, boxes, classes, scores, category_index, instance_masks=None, keypoints=None, use_normalized_coordinates=False,
                                              max_boxes_to_draw=20, min_score_thresh=.7, agnostic_mode=False, line_thickness=4):
    box_to_display_str_map = collections.defaultdict(list)
    box_to_color_map = collections.defaultdict(str)
    items = box_to_color_map.items()
    box_to_instance_masks_map = {}
    box_to_keypoints_map = collections.defaultdict(list)
    if not max_boxes_to_draw:
        max_boxes_to_draw = boxes.shape[0]
    for i in range(min(max_boxes_to_draw, boxes.shape[0])):
        if scores is None or scores[i] > min_score_thresh:
            box = tuple(boxes[i].tolist())
            if instance_masks is not None:
                box_to_instance_masks_map[box] = instance_masks[i]
            if keypoints is not None:
                box_to_keypoints_map[box].extend(keypoints[i])
            if scores is None:
                box_to_color_map[box] = 'black'
            else:
                if not agnostic_mode:
                    if classes[i] in category_index.keys():
                        class_name = category_index[classes[i]]['name']
                    else:
                        class_name = 'N/A'
                    display_str = '{}: {}%'.format(
                        class_name,
                        int(100 * scores[i]))
                else:
                    display_str = 'score: {}%'.format(int(100 * scores[i]))
                box_to_display_str_map[box].append(display_str)
                box_to_color_map[box] = (238, 130, 238)

    max_face = []
    max_volume = 0
    image = np.asanyarray(image)
    image_np = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    rgb_image = np.asanyarray(image_np)
    for box, color in items:
        ymin, xmin, ymax, xmax = box
        ymin, xmin, ymax, xmax = int(ymin * image.shape[0]), int(xmin * image.shape[1]), int(ymax * image.shape[0]), int(xmax * image.shape[1])
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 3)

        face = rgb_image[ymin:ymax, xmin:xmax]
        if (ymax - ymin) * (xmax - xmin) > max_volume:
            max_volume = (ymax - ymin) * (xmax - xmin)
            max_face = face

        square_coef = (ymax - ymin) * (xmax - xmin) / (image.shape[0] * image.shape[1])
        square_coef = round(square_coef, 5)
        text = f'sq_c: {square_coef}'
        font_face = cv2.LINE_AA
        font_scale = 1
        thickness = 2

        text_width, text_height = cv2.getTextSize(text, font_face, font_scale, thickness)[0]
        cv2.rectangle(image, (xmin-3, ymin-text_height), (xmin+text_width, ymin), color, -1)
        cv2.putText(image, text, (xmin, ymin - thickness), font_face, font_scale, (0, 0, 0), thickness, cv2.LINE_AA)

    square_coef = max_volume / (image.shape[0] * image.shape[1])
    return image, max_face, square_coef
