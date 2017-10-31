#Threshld help in simplify images edges
#Converting to Grayscale
#Threshold means 0 or 1, it also means gradient

import cv2
import numpy as np

img=cv2.imread('bookpage.jpg')

#Converting to 255 or not above threshold value but its not changed to grayscale
#so it will be converted to RGB of highest value 
retval, threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)

grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Converting to 255 or not in black and white but we are applying threshold
#manually. It may lead to reading of data or not
retval2, threshold2 = cv2.threshold(grayscale,12,255,cv2.THRESH_BINARY)

# Adaptive Gaussian Threshold
gaus=cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

retval,otsu=cv2.threshold(grayscale,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('img',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('gaus',gaus)
cv2.imshow('otsu',otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
