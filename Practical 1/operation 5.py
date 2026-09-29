import cv2
image1 = cv2.imread("ronaldo.jfif")
image2 = cv2.imread("ronaldo2.webp")
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
cv2.imshow("Weighted Image", weightedSum)
cv2.waitKey(0)
cv2.destroyAllWindows()
