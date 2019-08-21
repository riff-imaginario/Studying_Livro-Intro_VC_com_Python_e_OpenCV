import numpy as np
import cv2

img = cv2.imread('../../_img/terminator_hand.jpg')

cv2.imshow('Original', img)

largura = img.shape[1]
altura  = img.shape[0]

proporcao    = float(altura / largura)
largura_nova = 320  # pixels
altura_nova  = int(largura_nova * proporcao)

tamanho_novo = (largura_nova, altura_nova)

img_redimensionada = cv2.resize(img, tamanho_novo, interpolation = cv2.INTER_AREA)

cv2.imshow('Redimensionada', img_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()