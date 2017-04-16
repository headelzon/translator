import cv2
import numpy as np

# Open image
img = cv2.imread('002.jpg')

# Convert to gray and binarize
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 110, 255, cv2.THRESH_BINARY_INV)

# Get rid of small white pixels (opening)
kernel = np.ones((2, 2), np.uint8)
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Find contours
im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
M = cv2.moments(cnt)
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)

# Find angle of rotation of the bounding box
angle = rect[2]

# Find centroid
Cx = int(M['m10']/M['m00'])
Cy = int(M['m01']/M['m00'])
C = (Cx, Cy)

# Get rotation matrix
rot = cv2.getRotationMatrix2D(C, angle, 1)
tmp = thresh.shape
size = (tmp[1], tmp[0])     # Swap values in size matrix

# Rotate the image by the angle
rotated = cv2.warpAffine(thresh, rot, size)

# Write in as final.jpg
cv2.imwrite('final.jpg', rotated)
