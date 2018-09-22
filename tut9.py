import cv2
import numpy as np

cap = cv2.VideoCapture('Merida500Cuted.avi')
#cv2.namedWindow('frame', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('result', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
#cv2.namedWindow('erosion', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
#cv2.namedWindow('dilation', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('opening', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('closing', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('Tophat', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('Blackhat', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
while True:
	_, frame = cap.read()
	if frame is None:
		cap = cv2.VideoCapture('Merida500Cuted.avi')
		_, frame = cap.read()
	
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# hsv hue sat value
	lower_green = np.array([40,0,0]) #in hsv
	upper_green = np.array([86, 255, 255])
	
	mask = cv2.inRange(hsv, lower_green, upper_green)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	
	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations = 1)
	dilation = cv2.dilate(mask, kernel, iterations = 1)	
	
	#opening remove false-positive, background
	#closing remove false-negative
	
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	
	#cv2.imshow('frame', frame)
	cv2.imshow('result', res)
	#cv2.imshow('erosion', erosion)
	#cv2.imshow('dilation', dilation)
	cv2.imshow('opening', opening)
	cv2.imshow('closing', closing)
	
	# It is the difference between input image and Opening of the image
	# cv2.imshow('Tophat', tophat)
	
	# It is the difference between the closing of the input image and input image.
	# cv2.imshow('Blackhat', blackhat)
	
	
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break;

cv2.destroyAllWindows()
cap.release()