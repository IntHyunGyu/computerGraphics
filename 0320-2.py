import sys

import cv2 as cv

img = cv.imread('img/soccer.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다')

cv.imshow('img', img)

cv.waitKey()
cv.destroyAllWindows()