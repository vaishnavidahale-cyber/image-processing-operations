import cv2
import numpy as np
image1 = cv2.imread('ronaldo.jfif')
image2 = cv2.imread('ronaldo2.webp')
# Resize image2 to the size of image1
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
sub = cv2.subtract(image1, image2)
cv2.imshow('Subtracted Image', sub)
if cv2.waitKey(0) & 0xff == 27:
cv2.destroyAllWindows()

