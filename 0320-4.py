import cv2
import matplotlib.pyplot as plt

img=cv2.imread('img/soccer.jpg')
h=cv2.calcHist([img],[2],None,[256],[0,256])
plt.plot(h,color='r',linewidth=1)
