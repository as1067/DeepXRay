import cv2
from label_reader import LabelReader
image = cv2.imread("images/00000001_000.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image,(448,448))
l = LabelReader()
annotations = l.read()
