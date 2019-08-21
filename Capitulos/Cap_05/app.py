import cv2
import numpy as np

img = cv2.imread('../../_img/terminator_hand.jpg')
cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) cv2.imshow("Gray", gray)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) cv2.imshow("HSV", hsv)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) cv2.imshow("L*a*b*", lab)

cv2.waitKey(0)
