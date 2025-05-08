import numpy as np
import cv2 as cv

image = np.zeros((200, 300), np.uint8)
image.fill(255)

title1, title2 = 'AUTOSIZE', 'NORMAL'
cv.namedWindow(title1, cv.WINDOW_AUTOSIZE)
cv.namedWindow(title2, cv.WINDOW_NORMAL)

cv.imshow(title1, image)
cv.imshow(title2, image)
cv.resizeWindow(title1, 400, 300)
cv.resizeWindow(title2, 400, 300)

cv.waitKey(0)
cv.destroyAllWindows()