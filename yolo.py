import os
import cv2

def detect(image_path):
    os.system("cd /yolo-9000/darknet;/yolo-9000/darknet/darknet detector test /yolo-9000/darknet/cfg/combine9k.data /yolo-9000/darknet/cfg/yolo9000.cfg /yolo-9000/yolo9000-weights/yolo9000.weights {}".format(image_path))
    img = cv2.imread("/yolo-9000/darknet/predictions.png")
    return img