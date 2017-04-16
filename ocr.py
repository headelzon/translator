from PIL import Image
import pytesseract
import cv2
import numpy as np
from matplotlib import pyplot as plt


reading = pytesseract.image_to_string(Image.open('lines.jpg'))

print(reading)

f = open('reading.txt', 'w+')
f.write(reading)
f.close()
