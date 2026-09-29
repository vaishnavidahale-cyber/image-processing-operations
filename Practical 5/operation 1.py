import cv2
import numpy as np

# -------------------------------
# PART 1: Generate mask & restore using TELEA
# -------------------------------
# Step 1: Read the damaged image
damaged_img = cv2.imread("girl.png")

# Step 2: Create mask from damaged image
height, width = damaged_img.shape[0], damaged_img.shape[1]

# Convert to grayscale to check brightness levels easily
gray_img = cv2.cvtColor(damaged_img, cv2.COLOR_BGR2GRAY)

mask = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        # The damage (smiley face) is white, so check if gray intensity is near white (> 240)
        if gray_img[i, j] > 240:  # damaged white pixel → white in mask
            mask[i, j] = [255, 255, 255]
        else:  # non-damaged pixel → black in mask
            mask[i, j] = [0, 0, 0]

# Convert mask to grayscale
mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

# Save mask
cv2.imwrite("generated_mask.jpg", mask_gray)

# Step 3: Perform inpainting (TELEA method)
restored_telea = cv2.inpaint(damaged_img, mask_gray, 3, cv2.INPAINT_TELEA)


# -------------------------------
# PART 2: Use predefined mask & restore using NS
# -------------------------------
# Step 4: Read damaged image again
img = cv2.imread("girl.png")

# Step 5: Load predefined mask (must be a binary image saved from step 2)
mask_predefined = cv2.imread("generated_mask.jpg", 0)

# Step 6: Inpaint with Navier-Stokes method
restored_ns = cv2.inpaint(img, mask_predefined, 3, cv2.INPAINT_NS)

# Save results
cv2.imwrite("restored_telea.png", restored_telea)
cv2.imwrite("restored_ns.png", restored_ns)

# -------------------------------
# Display Results
# -------------------------------
cv2.imshow("Original Damaged Image", damaged_img)
cv2.imshow("Generated Mask", mask_gray)
cv2.imshow("Restored (Telea)", restored_telea)
cv2.imshow("Predefined Mask", mask_predefined)
cv2.imshow("Restored (Navier-Stokes)", restored_ns)

cv2.waitKey(0)
cv2.destroyAllWindows()