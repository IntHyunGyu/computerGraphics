import numpy as np
import cv2 as cv

image1 = np.zeros((300,300), np.uint8)
image2 = image1.copy()

h, w = image1.shape[:2]
cx, cy = w//2, h//2
cv.circle(image1,(cx,cy), 100, 255, -1)
cv.rectangle(image2,(0,0,cx,h),255,-1)

image3 = cv.bitwise_or(image1,image2)
image4 = cv.bitwise_and(image1,image2)
image5 = cv.bitwise_xor(image1,image2)
image6 = cv.bitwise_not(image1)

cv.imshow('image1', image1)
cv.imshow('image2', image2)
cv.imshow('bitwise_or', image3)
cv.imshow('bitwise_and', image4)
cv.imshow('bitwise_xor', image5)
cv.imshow('bitwise_not', image6)
cv.waitKey(0)