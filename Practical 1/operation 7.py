import numpy as np
img1 = cv2.imread('ronaldo.jfif')
img2 = cv2.imread('ronaldo2.webp')
# Resize img2 to match img1
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
dest_and = cv2.bitwise_and(img2, img1, mask=None)
cv2.imshow('Bitwise And', dest_and)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

