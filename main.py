from PIL import Image
import pytesseract
import cv2
import numpy as np
from matplotlib import pyplot as plt


# 1. Read image
# 2. Binarize the image, text white, background black
# 3. Remove noise
# 4. Extract bounding box of the text
# 5. Rotate to vertical
# 6. Split pictures into lines of text
# 7. Read the lines
# 8. Output into txt file

img = cv2.imread('002.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

# plt.hist(gray_img.ravel(), 256, [0, 256])
# plt.show()

ret, thresh1 = cv2.threshold(gray_img, 110, 255, cv2.THRESH_BINARY_INV)

# cv2.imwrite('binary.jpg', thresh1)

lines = cv2.HoughLines(thresh1, 1, np.pi/180, 200)
cv2.imwrite('lines.jpg', lines)


# reading = pytesseract.image_to_string(Image.open('binary.jpg'), lang='deu')
#
# print(reading)
#
# f = open('reading.txt', 'w+')
# f.write(reading)
# f.close()
