import numpy as np
import cv2

img=cv2.imread('nature.jpg',cv2.IMREAD_COLOR)

img[48,56]=[255,255,255]
img[100:150,100:150]=[0,0,0]
#copy and paste part of image

watch=img[350:100,280:200]
img[250:0,80:0]=watch

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
