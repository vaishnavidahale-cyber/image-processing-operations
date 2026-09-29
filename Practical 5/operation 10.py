import cv2
import matplotlib.pyplot as plt

# Read the generated noisy image (or change to "girl.png")
img = cv2.imread("noisy_gaussian.png", 0)

# Check if the image was actually loaded
if img is None:
    print("Error: Could not load image. Make sure 'noisy_gaussian.png' or 'girl.png' exists in your working directory.")
else:
    # Apply Gaussian Blur to restore
    restored = cv2.GaussianBlur(img, (5, 5), 0)

    # Show results
    plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray'), plt.title("Gaussian Noisy")
    plt.subplot(1, 2, 2), plt.imshow(restored, cmap='gray'), plt.title("Restored (Gaussian Blur)")
    plt.show()