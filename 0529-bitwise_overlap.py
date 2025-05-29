import numpy as np
import cv2 as cv

image = cv.imread('img/bit_test.jpg', cv.IMREAD_COLOR)
logo = cv.imread('img/logo.jpg', cv.IMREAD_COLOR)
if image is None or logo is None: raise Exception('영상파일 읽기 오류')

masks = cv.threshold(logo, 220, 255, cv.THRESH_BINARY)[1]
masks = cv.split(masks)

fg_pass_mask = cv.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv.bitwise_or(masks[2], fg_pass_mask)
bg_pass_mask = cv.bitwise_not(fg_pass_mask)
(H, W), (h, w) = image.shape[:2], logo.shape[:2]
x, y = (W-w)//2, (h-h)//2
roi = image[y:y+h, x:x+w]

foreground = cv.bitwise_and(logo, logo, mask=fg_pass_mask)
background = cv.bitwise_and(roi, roi, mask=bg_pass_mask)

dst = cv.add(background, foreground)
image[y:y+h, x:x+w] = dst

cv.imshow('backgroud', background)
cv.imshow('foreground', foreground)
cv.imshow('dst', dst)
cv.imshow('image', image)
cv.waitKey(0)
