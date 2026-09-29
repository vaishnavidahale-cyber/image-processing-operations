import cv2
import numpy as np

# ---------- Load the image ----------
image_path = 'panda.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Image not found. Check the path.")

# ---------- Threshold to ensure binary ----------
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# ---------- Define structuring element ----------
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# ---------- Erosion ----------
erosion = cv2.erode(binary, kernel, iterations=1)

# ---------- Dilation ----------
dilation = cv2.dilate(binary, kernel, iterations=1)

# ---------- Opening ----------
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# ---------- Closing ----------
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# ---------- Display Results ----------
cv2.imshow("Original Binary(CS24246)", binary)
cv2.imshow("Erosion(CS24246)", erosion)
cv2.imshow("Dilation(CS24246)", dilation)
cv2.imshow("Opening(CS24246)", opening)
cv2.imshow("Closing(CS24246)", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()