import cv2
import numpy

# Read the input image
img = cv2.imread("harry.jpg")

# Apply Gaussian filter
dst = cv2.GaussianBlur(
    img,
    (5, 5),
    cv2.BORDER_DEFAULT
)

# Display original and filtered image side by side
cv2.imshow(
    'Vaishnavi(CS24246)',
    numpy.hstack((img, dst))
)

cv2.waitKey(0)
cv2.destroyAllWindows()