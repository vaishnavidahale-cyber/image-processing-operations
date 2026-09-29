import cv2
import numpy as np
img1 = cv2.imread('emma.jfif')
img2 = cv2.imread('emma2.jfif')
# Resize img2 to match the exact dimensions (width, height) of img1
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
dest_xor = cv2.bitwise_xor(img1, img2, mask=None)
cv2.imshow('Bitwise XOR', dest_xor)
# Wait for any key press, then close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
