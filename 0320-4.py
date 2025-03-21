import sys

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img/soccer.jpg')
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

h = cv2.calcHist([img],[2],None,[256],[0,256])
plt.plot(h, color='r', linewidth=1)
plt.show()

