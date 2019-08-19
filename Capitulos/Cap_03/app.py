import numpy as np
import cv2

imagem = cv2.imread('../../_img/terminator_hand.jpg')
fonte = cv2.FONT_HERSHEY_SIMPLEX

# Adiciona texto a imagem
cv2.putText(imagem,'OpenCV',(15,65), fonte, 2,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("Image", imagem)
cv2.waitKey(0)