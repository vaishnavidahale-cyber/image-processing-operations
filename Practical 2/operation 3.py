import numpy as np
import cv2 as cv

img = cv.imread('shinchan.jfif', 0)

if img is None:
    print("Image not found!")
else:
    rows, cols = img.shape

    img_rotation = cv.warpAffine(
        img,
        cv.getRotationMatrix2D((cols / 2, rows / 2), 30, 0.6),
        (cols, rows)
    )

    cv.imshow('Vaishnavi(CS24246)', img_rotation)

    cv.imwrite('rotation_out.jpg', img_rotation)

    cv.waitKey(0)
    cv.destroyAllWindows()