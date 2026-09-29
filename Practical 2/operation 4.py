import numpy as np
import cv2 as cv

img = cv.imread('shinchan.jfif', 0)

if img is None:
    print("Image not found!")
else:
    img_shrinked = cv.resize(
        img,
        (250, 200),
        interpolation=cv.INTER_AREA
    )

    cv.imshow("Shrinked Image", img_shrinked)

    img_enlarged = cv.resize(
        img_shrinked,
        None,
        fx=1.5,
        fy=1.5,
        interpolation=cv.INTER_CUBIC
    )

    cv.imshow("Enlarged Image", img_enlarged)

    cv.waitKey(0)
    cv.destroyAllWindows()