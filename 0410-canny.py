import cv2 as cv

img=cv.imread('img/soccer.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny1 = cv.Canny(gray, 50, 150)
canny2 = cv.Canny(gray, 100, 200)
canny3 = cv.Canny(gray, 150, 250)
canny4 = cv.Canny(gray, 200, 300)

cv.imshow('Original', gray)
cv.imshow('canny 1', canny1)
cv.imshow('canny 2', canny2)
cv.imshow('canny 3', canny3)
cv.imshow('canny 4', canny4)

cv.waitKey(0)
cv.destroyAllWindows()