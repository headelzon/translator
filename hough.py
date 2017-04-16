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
Cx = int(M['m10'] / M['m00'])
Cy = int(M['m01'] / M['m00'])
C = (Cx, Cy)

# Get rotation matrix
rot = cv2.getRotationMatrix2D(C, angle, 1)
tmp = thresh.shape
size = (tmp[1], tmp[0])  # Swap values in size matrix

# Rotate the image by the angle
rotated = cv2.warpAffine(img, rot, size)
rotated_bw = cv2.warpAffine(thresh, rot, size)

# Find contours
im2, contours, hierarchy = cv2.findContours(rotated_bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cnt = contours[0]

x, y, w, h = cv2.boundingRect(cnt)
crop_img = rotated[y:y + h, x:x + w]  # Crop from x, y, w, h -> 100, 200, 300, 400
cropped_bw = rotated_bw[y:y + h, x:x + w]

# HOUGH LINES

cv2.imwrite('edges.jpg', cropped_bw)

minLineLength = 10
maxLineGap = 10
lines = cv2.HoughLinesP(cropped_bw, 1, np.pi/2, 50, minLineLength, maxLineGap)

# for line in lines:
#     for rho, theta in line:
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a * rho
#         y0 = b * rho
#         x1 = int(x0 + 1000 * (-b))
#         y1 = int(y0 + 1000 * a)
#         x2 = int(x0 - 1000 * (-b))
#         y2 = int(y0 - 1000 * a)
#
#         cv2.line(crop_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(crop_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imwrite('lines.jpg', crop_img)

# TODO Still doesn't detect every edge
# TODO Rotate image to make its sides parallel to axes

# TODO Extract information from rows and columns
