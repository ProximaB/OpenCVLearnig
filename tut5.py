import cv2
import numpy as np
img1 = cv2.imread('merida.jpg')
img2 = cv2.imread('image.jpeg')
img1_inSizeImg2 = img1[0:172, 0:293]
add = img1_inSizeImg2 + img2

cv2.imshow('add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()