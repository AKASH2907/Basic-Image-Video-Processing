#Multiple Different types of morphological transformations pairwise analysis
#Erosion and Dilation
#Erosion  Slider(manually sized) if every pixel value is same then do nothing
#if different then erodes that different pixel value if diffrent in neighbourhood
#Dilation pushes it out thru until it cant more push out
#opening remove false positives
#closing remove false negatives
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame=cap.read()
    #Hue saturation value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower=np.array([50,150,0])
    upper=np.array([255,255,255])

    mask=cv2.inRange(hsv,lower,upper)
    res= cv2.bitwise_and(frame,frame,mask=mask)

    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask, kernel, iterations=1)
    dilation=cv2.dilate(mask, kernel, iterations=1)
    #In dilation noise is more a bit amplified
    
    opening=cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing=cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('frame',frame)
    cv2.imshow('erosion',erosion)
    #cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)
    

    if (cv2.waitKey(5) & 0xff)==27:
        break


cv2.destroyAllWindows()
cap.release()
