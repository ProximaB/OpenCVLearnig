import cv2
import numpy as np
img1 = cv2.imread('merida.jpg')
img2 = cv2.imread('image.jpeg')
img1_inSizeImg2 = img1[0:172, 0:293]
#add = img1_inSizeImg2 + img2
# (155,211,79) + (50,170,200) = 205, 381, 279...translated to (205,255,255)
#add = cv2.add(img1_inSizeImg2*2, img2*2) #add = cv2.add(img1_inSizeImg2*2, img2*2)
#weighted = cv2.addWeighted(img1_inSizeImg2, 0.6, img2, 0.4, 0)
#cv2.imshow('weighted', weighted)

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv) #or xor
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dist = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dist
cv2.imshow('res', img1)

cv2.waitKey(10*1000)
cv2.destroyAllWindows()