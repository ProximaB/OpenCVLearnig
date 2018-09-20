import cv2
import numpy as np

#cap = cv2.VideoCaputre(0)
cap = cv2.VideoCapture('Merida500.mp4')
cv2.namedWindow('Podglad obrazu', cv2.WINDOW_GUI_EXPANDED)
#cv2.namedWindow('Podglad obrazu szary', cv2.WINDOW_GUI_EXPANDED)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Merida500Cuted.avi', fourcc, 20.0, (1280 , 720))
while True:
	ret, frame = cap.read()
	cv2.imshow('Podglad obrazu', frame)
	if cv2.waitKey(1) & 0xFF == ord('s'):
		out.write(frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break	
		
cap.release()
out.release()
cv2.destroyAllWindows()
