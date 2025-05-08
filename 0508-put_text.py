import cv2 as cv
import numpy as np

olive, violet, brown = (128, 0, 0), (211, 160, 221), (42, 42, 165)
pt1, pt2 = (50, 200), (50, 260)

image = np.zeros((350, 500, 3), np.uint8)
image.fill(255)

cv.putText(image, 'SIMLEX', (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, brown)
cv.putText(image, 'DUPLEX', (50, 130), cv.FONT_HERSHEY_DUPLEX, 2, olive)
cv.putText(image, 'TRIPLEX', pt1, cv.FONT_HERSHEY_TRIPLEX, 2, violet)
fontFace = cv.FONT_HERSHEY_PLAIN | cv.FONT_ITALIC
cv.putText(image, 'ITALIC', pt2, fontFace, 4, violet)

cv.imshow('Put Text', image)
cv.waitKey(0)