import cv2
import numpy as np

def detect_object(template_path, input_image_path):

    # Read the template and input image
    template = cv2.imread(template_path, 0)
    img = cv2.imread(input_image_path)

    if template is None or img is None:
        raise FileNotFoundError("Image not found. Check the file path.")

    # Convert input image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Get height and width of template
    h, w = template.shape[:2]

    # Perform template matching
    res = cv2.matchTemplate(
        gray_img,
        template,
        cv2.TM_CCOEFF_NORMED
    )

    # Set threshold
    threshold = 0.8

    # Find locations where match is above threshold
    loc = np.where(res >= threshold)

    # Draw rectangles around matched areas
    for pt in zip(*loc[::-1]):
        cv2.rectangle(
            img,
            pt,
            (pt[0] + w, pt[1] + h),
            (0, 255, 255),
            2
        )

    # Display result
    cv2.imshow("Detected Objects(CS24246)", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Provide paths to template and input images
template_path = "all of us are dead2 final.png"
input_image_path = "all of us are dead final.png"

# Detect the object
detect_object(template_path, input_image_path)