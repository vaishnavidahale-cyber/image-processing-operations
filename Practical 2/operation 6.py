import numpy as np
import cv2 as cv

img = cv.imread('shinchan.jfif', 0)

if img is None:
    print("Image not found!")
else:
    rows, cols = img.shape

    M = np.float32([
        [1, 0.5, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    sheared_img = cv.warpPerspective(
        img,
        M,
        (int(cols * 1.5), int(rows * 1.5))
    )

    cv.imshow("Sheared Image", sheared_img)

    cv.waitKey(0)
    cv.destroyAllWindows()