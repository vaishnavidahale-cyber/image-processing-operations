import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Read the damaged image
# -------------------------------
damaged_img = cv2.imread("girl.png")

# -------------------------------
# Step 2: Create mask automatically
# -------------------------------
height, width = damaged_img.shape[0], damaged_img.shape[1]

# Convert to grayscale to evaluate pixel brightness
gray_img = cv2.cvtColor(damaged_img, cv2.COLOR_BGR2GRAY)

mask_auto = np.zeros((height, width, 3), dtype=np.uint8)
for i in range(height):
    for j in range(width):
        # Scratch is white, so check if intensity is near white (> 240)
        if gray_img[i, j] > 240:   # damaged white pixel → white in mask
            mask_auto[i, j] = [255, 255, 255]
        else:  # non-damaged pixel → black in mask
            mask_auto[i, j] = [0, 0, 0]

# Convert mask to grayscale
mask_auto_gray = cv2.cvtColor(mask_auto, cv2.COLOR_BGR2GRAY)

# Save mask so it can be used as a predefined mask file
cv2.imwrite("generated_mask.jpg", mask_auto_gray)

# -------------------------------
# Step 3: Restore with TELEA method
# -------------------------------
restored_telea = cv2.inpaint(damaged_img, mask_auto_gray, 3, cv2.INPAINT_TELEA)

# -------------------------------
# Step 4: Restore with Predefined Mask using NS method
# -------------------------------
mask_predefined = cv2.imread("generated_mask.jpg", 0)  # Load saved mask file
restored_ns = cv2.inpaint(damaged_img, mask_predefined, 3, cv2.INPAINT_NS)

# -------------------------------
# Step 5: Plot results using Matplotlib
# -------------------------------
images = [damaged_img, mask_auto_gray, restored_telea, restored_ns]
titles = ["Original Damaged", "Generated Mask", "Restored (Telea)", "Restored (Navier-Stokes)"]

plt.figure(figsize=(10, 10))  # Adjust window size as needed

for i in range(4):
    plt.subplot(2, 2, i+1)
    if len(images[i].shape) == 2:   # grayscale (mask)
        plt.imshow(images[i], cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # convert BGR → RGB
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()