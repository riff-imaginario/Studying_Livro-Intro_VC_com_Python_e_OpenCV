import cv2

img = cv2.imread('../../_img/terminator_hand.jpg')

recorte = img[25:50, 25:50]  # slicing para cortar imagem

cv2.imshow('Recorte', recorte)
cv2.imwrite('recorte.jpg', recorte)
