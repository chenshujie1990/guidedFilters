from cv2 import cv2
from baseline import imguidedFilter

img = cv2.imread(".\\imgs\\1.jpg")
img_noised = cv2.imread(".\\imgs\\1n.jpg")

img_filtered = imguidedFilter(img_noised, img_noised, smoothing=1, win=(5,5))

cv2.imshow('original image', img)
cv2.imshow('noised image', img_noised)
cv2.imshow('baseline guided filtering result', img_filtered)
cv2.waitKey(0)
