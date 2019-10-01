import cv2

image = cv2.imread("images/00000001_000.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image,(448,448))
cv2.imshow("image",image)
cv2.waitKey(0)