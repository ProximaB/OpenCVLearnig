import cv2
import numpy as np

cap = cv2.VideoCapture('Merida500Cuted.avi')
cv2.namedWindow('frame', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('result', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('erosion', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('dilation', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
while True:
	_, frame = cap.read()
	if frame is None:
		cap = cv2.VideoCapture('Merida500Cuted.avi')
		_, frame = cap.read()
	
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# hsv hue sat value
	lower_green = np.array([0,112,0])
	upper_green = np.array([190, 255, 230])
	
	mask = cv2.inRange(hsv, lower_green, upper_green)
	res = cv2.bitwise_and(frame, frame, mask = mask)
	
	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations = 1)
	dilation = cv2.dilate(mask, kernel, iterations = 1)	
	
	
	cv2.imshow('frame', frame)
	cv2.imshow('result', res)
	cv2.imshow('erosion', erosion)
	cv2.imshow('dilation', dilation)
	
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break;

cv2.destroyAllWindows()
cap.release()