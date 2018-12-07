import cv2
from matplotlib import pyplot as plt


image = cv2.imread("spidermorales.jpg",0)
plt.hist(image.ravel(),256,[0,256])

cv2.imshow('image',image)
plt.show()

k = cv2.waitKey(0) & 0xFF
if k == 27:
	cv2.destroyAllWindows()
