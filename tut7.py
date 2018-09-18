import cv2
import numpy as np

cap = cv2.VideoCapture('Merida500.mp4')

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# hsv hue sat value
	lower_green = np.array([0,200,90])
	upper_green = np.array([128, 250, 195])
	
	mask = cv2.inRange(hsv, lower_green, upper_green)
	res = cv2.bitwise_and(frame, frame, mask = mask)
	cv2.circle(res, (100,63), 55, (90,200,0), -1)
	cv2.circle(res, (155,63), 55, (110,237,0), -1)
	cv2.circle(res, (210,63), 55, (195,250,128), -1)
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