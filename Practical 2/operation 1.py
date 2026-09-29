import numpy as np
import cv2 as cv

img = cv.imread('shinchan.jfif', 0)

if img is None:
    print("Image not found!")
else:
    rows, cols = img.shape

    M = np.float32([[1, 0, 100],
                    [0, 1, 50]])

    dst = cv.warpAffine(img, M, (cols, rows))

    cv.imshow('Vaishnavi(CS24246)', dst)

    cv.waitKey(0)
    cv.destroyAllWindows()