import numpy as np
import cv2

img = cv2.imread('merida.jpg', cv2.IMREAD_COLOR)

img[55,55] = [0,255,255]
px = img[55, 55]

img[100:150, 100:150] =  [255, 255, 0]
#print(roi)

fragment = img[37:420, 107:194]
img[0:343, 0:87] = fragment

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()