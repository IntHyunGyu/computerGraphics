import cv2 as cv
import numpy as np

def onmouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 버튼 누르기")
    elif event == cv.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽 버튼 누르기")
    elif event == cv.EVENT_LBUTTONUP:
        print("마우스 왼쪽 버튼 때기")
    elif event == cv.EVENT_RBUTTONUP:
        print("마우스 오른쪽 버튼 때기")
    elif event == cv.EVENT_LBUTTONDBLCLK:
        print("마우스 왼쪽 버튼 더블클릭")

image = np.full((200, 300), 255, np.uint8)

title1, title2 = "Mouse Event1", "Mouse Event2"
cv.imshow(title1, image)
cv.imshow(title2, image)

cv.setMouseCallback(title1, onmouse)
cv.waitKey(0)
cv.destroyAllWindows()