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

    lower=np.array([150,150,50])
    upper=np.array([180,255,180])

    mask=cv2.inRange(hsv,lower,upper)
    res= cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    if (cv2.waitKey(5) & 0xff)==27:
        break


cv2.destroyAllWindows()
cap.release()
