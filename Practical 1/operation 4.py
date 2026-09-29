import cv2
path = r'ronaldo.jfif'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Vaishnavi(CS24246)', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
