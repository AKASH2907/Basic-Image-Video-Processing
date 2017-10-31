import cv2
import numpy as np

#Filter image or video to find a specific color or remove a specific color
#Only show specific color or without it
#Sort of filter using bitwise
cap = cv2.VideoCapture(0)

while True:
    _, frame=cap.read()
    #Hue saturation value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower=np.array([50,150,0])
    upper=np.array([255,255,255])

    mask=cv2.inRange(hsv,lower,upper)
    res= cv2.bitwise_and(frame,frame,mask=mask)

    #Average kernel of 15*15 matrix of 1s filtering over image to remove the 
    #effect of noise.Not of use much
    kernel=np.ones((15,15),np.float32)/225
    smooth=cv2.filter2D(res,-1,kernel)

    #Gaussian filter blur
    blur = cv2.GaussianBlur(res, (15,15), 0)
    #Median blur mostly better than others
    median = cv2.medianBlur(res,15)
    #bilateral blur
    bilateral=cv2.bilateralFilter(res,15,75,75)
    
    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    #cv2.imshow('smooth',smooth)
    cv2.imshow('blur',blur)
    cv2.imshow('median',median)
    cv2.imshow('bilateral',bilateral)

    if (cv2.waitKey(5) & 0xff)==27:
        break


cv2.destroyAllWindows()
cap.release()
