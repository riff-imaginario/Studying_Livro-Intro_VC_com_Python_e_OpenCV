import cv2

img = cv2.imread('../../_img/terminator_hand.jpg')

for i in range(0, img.shape[0], 10):
    for j in range(0, img.shape[1], 10):
        img[i:i+2, j:j+2] = (0, 255, 255)

cv2.imshow('Mod', img)
cv2.waitKey(0)