import cv2
import numpy as np

img = cv2.imread('book.jpg') #above 160 white, under black
retval, threshold = cv2.threshold(img, 130 , 255, cv2.THRESH_BINARY)

cv2.imshow('optional', img)
cv2.imshow('threshold', threshold)
cv2.waitKey(0)
cv2.destroyAllWinows() 