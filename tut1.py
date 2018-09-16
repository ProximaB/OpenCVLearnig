import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

def loadImage( str ):
	print('Proba zaladowania obrazu: '  + str)
	img = cv2.imread(str)
	if img is None:
		print('Obraz nie został załadowany.')
		return None
	return img;
	
def showImage( img ):
	try:
		cv2.imshow('Image', img)
	except Exception as e:
		print('Nie udalo sie wyswietlic obrazu.')
		print('Exception: ' + str(e))
		sys.exit(0)

img = loadImage('merida.jpg')
showImage(img)

plt.figure(dpi=300)
plt.imshow(img)#, cmap='RdYlGn', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(10 * 1000)
cv2.destroyAllWindows()

