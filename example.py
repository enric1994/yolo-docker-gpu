import os
import cv2
import yolo

image = yolo.detect('/yolo/test.png')
cv2.imwrite('result.png', image)