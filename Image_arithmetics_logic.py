import cv2
import numpy as np

img1=cv2.imread('nature.jpg',cv2.IMREAD_COLOR)
img2=cv2.imread('test.jpg',cv2.IMREAD_COLOR)

#add=img1+img2 superimposing image of same size on each other
#add=cv2.add(img1,img2) adding pixel by pixel value of each image
#weight=cv2.addWeighted(img1,0.9,img2,0.5,0) weighted superimposing

#cv2.imshow('weight',weight)

rows,cols,channels= img2.shape
roi=img1[10:rows+10,10:cols+10]

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
#150,255 denotesthat any pixel value above 150 will be converted to
#255 otherwise black

mask_inv=cv2.bitwise_not(mask)
#inverse of the above mask white->black and vice versa

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
#bckground of img1 
img2_fg=cv2.bitwise_and(img2,img2,mask=mask)

dst=cv2.add(img1_bg,img2_fg)
img1[10:rows+10,10:cols+10]=dst

cv2.imshow('mask_inv',mask_inv)
cv2.imshow('mask',mask)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('dst',dst)
cv2.imshow('res',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
