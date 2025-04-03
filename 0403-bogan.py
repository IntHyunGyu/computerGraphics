import cv2 as cv

img=cv.imread('img/rose.png')
patch=img[250:350,170:270,:]

img=cv.rectangle(img,(170,250),(270,350),(255,0,0),3)
patch2=cv.resize(patch,dsize=(0,0),fx=5,fy=5, interpolation=cv.INTER_AREA)

cv.imshow('Original',img)
cv.imshow('Resize bilinear',patch2)

cv.waitKey()
cv.destroyAllWindows()