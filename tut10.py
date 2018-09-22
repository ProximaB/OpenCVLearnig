import cv2
import numpy as np

cap = cv2.VideoCapture('Merida500Cuted.avi')
cv2.namedWindow('origianal', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('laplacian', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('sobelx', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('sobely', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)

while True:
	_, frame = cap.read()
	if frame is None:
		cap = cv2.VideoCapture('Merida500Cuted.avi')
		_, frame = cap.read()
	
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5) #ksize kernel size
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
	
	cv2.imshow('origianal', frame)
	cv2.imshow('laplacian', laplacian)
	cv2.imshow('sobelx', sobelx)	
	cv2.imshow('sobely', sobely)
	
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break;

	
cv2.destroyAllWindows()
cap.release()