import cv2

# Step 1: Read the input image
image = cv2.imread('harry.jpg')

# Step 2: Set the kernel size
# Must be an odd positive integer
kernel_size = 5

# Step 3: Apply the median filter
filtered_image = cv2.medianBlur(image, kernel_size)

# Step 4: Display the original image
cv2.imshow('Original Image(CS24246)', image)

# Display the filtered image
cv2.imshow(
    'Filtered Image (Median Blur)',
    filtered_image
)

# Step 5: Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()