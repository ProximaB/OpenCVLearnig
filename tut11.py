import cv2
import numpy as np
import string
#[::-1] reverse matrix, [:-1] deleta last element
img_bgr = cv2.imread('merida.jpg')
img_bgr.astype(np.float32)
print('img_bgr size: '+ str(img_bgr.shape[::-1]))

img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
img_gray.astype(np.float32)
print('img_gray size: '+ str(img_gray.shape))
 
template = cv2.imread('meridaXchar.jpg', 0)
template.astype(np.float32)
print('template size: ' +  str(template.shape))

w, h = template.shape
 
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.72
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
	
cv2.imshow('deteted', img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindwos()
