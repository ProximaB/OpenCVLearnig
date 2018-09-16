import numpy as np
import cv2

img = cv2.imread('image.jpeg', 0)

cv2.namedWindow('Podglad obrazu', cv2.WINDOW_GUI_EXPANDED)
cv2.imshow('Podglad obrazu', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
