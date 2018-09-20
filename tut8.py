import cv2
import numpy as np

cap = cv2.VideoCapture('Merida500Cuted.avi')

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# hsv hue sat value
	lower_green = np.array([30,180,30])
	upper_green = np.array([188, 250, 195])
	
	mask = cv2.inRange(hsv, lower_green, upper_green)
	res = cv2.bitwise_and(frame, frame, mask = mask)
	cv2.circle(res, (100,63), 55, (30,180,30), -1)
	cv2.circle(res, (155,63), 55, (110,237,0), -1)
	cv2.circle(res, (210,63), 55, (195,250,188), -1)
	cv2.namedWindow('frame', cv2.WINDOW_GUI_EXPANDED)
	cv2.namedWindow('mask', cv2.WINDOW_GUI_EXPANDED)
	cv2.namedWindow('result', cv2.WINDOW_GUI_EXPANDED)
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('result', res)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break;

cv2.destroyAllWindows()
cap.release()
print('waitKey')