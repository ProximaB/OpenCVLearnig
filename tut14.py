import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img1 = cv2.imread('zegarek.jpeg', 0)

img2 = cv2.imread('zegarek_close.jpeg', 0)


orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img2 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:9], None, flags=2)
plt.imshow(img2)
plt.show()
while True:
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		cv2.destroyAllWindows()
		sys.exit(0)
		break;