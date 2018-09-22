import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('zegarek.jpeg', 1)

img2 = cv2.imread('zegarek_close.jpeg', 1)


orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img2 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:4], None, flags=2)
plt.imshow(img2)
plt.show()

cv2.waitKey(0)
