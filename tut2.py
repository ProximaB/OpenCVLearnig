import cv2
import numpy as np

#cap = cv2.VideoCaputre(0)
cap = cv2.VideoCapture('jellyfish.3gp')
cv2.namedWindow('Podglad obrazu', cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow('Podglad obrazu szary', cv2.WINDOW_GUI_EXPANDED)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	out.write(frame)
	cv2.imshow('Podglad obrazu', frame)
	
	cv2.imshow('Podglad obrazu szary' , gray)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break	
		
cap.release()
out.release()
cv2.destroyAllWindows()
