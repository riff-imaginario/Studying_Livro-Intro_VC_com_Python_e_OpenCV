import cv2

img = cv2.imread('../../_img/terminator_hand.jpg')

for i in range(0, img.shape[0], 1):
    for j in range(0, img.shape[1], 1):
        img[i, j] = (0, (i * j) % 256, 0)

cv2.imshow('Mod', img)
cv2.waitKey(0)