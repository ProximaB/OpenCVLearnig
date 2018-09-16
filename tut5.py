import cv2
import numpy as np
img1 = cv2.imread('merida.jpg')
img2 = cv2.imread('image.jpeg')
img1_inSizeImg2 = img1[0:172, 0:293]
#add = img1_inSizeImg2 + img2
# (155,211,79) + (50,170,200) = 205, 381, 279...translated to (205,255,255)
#add = cv2.add(img1_inSizeImg2*2, img2*2) #add = cv2.add(img1_inSizeImg2*2, img2*2)
#weighted = cv2.addWeighted(img1_inSizeImg2, 0.6, img2, 0.4, 0)
cv2.imshow('weighted', weighted)
cv2.waitKey(10*1000)
cv2.destroyAllWindows()