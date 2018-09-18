import cv2
import numpy as np

cap = cv2.VideoCapture('Merida500.mp4')

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	lower_green = np.array([0,0,0])
	upper_green = np.array([255, 255, 255])

cap.release()
cv2.waitKey(5*1000)
print('waitKey')
cv2.destroyAllWindows()