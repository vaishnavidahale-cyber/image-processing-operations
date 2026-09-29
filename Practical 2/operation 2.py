import numpy as np
import cv2 as cv

img = cv.imread('shinchan.jfif', 0)

if img is None:
    print("Image not found!")
else:
    rows, cols = img.shape

    M = np.float32([[1, 0, 0],
                    [0, -1, rows],
                    [0, 0, 1]])

    reflected_img = cv.warpPerspective(
        img, M, (int(cols), int(rows))
    )

    cv.imshow('Vaishnavi(CS24246)', reflected_img)

    cv.imwrite('reflection_out.jpg', reflected_img)

    cv.waitKey(0)
    cv.destroyAllWindows()