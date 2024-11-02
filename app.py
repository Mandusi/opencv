import cv2 as cv 

img = cv.imread('photos/f16.jpg')

img_resized = cv.resize(img, (800,600))

cv.rectangle(img_resized, (20,30), (700,540), thickness=2, color=(200,200,12))

cv.imshow('F-4', img_resized)

cv.waitKey(0)

