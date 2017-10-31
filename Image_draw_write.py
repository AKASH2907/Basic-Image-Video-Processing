import numpy as np
import cv2

img= cv2.imread('nature.jpg',cv2.IMREAD_UNCHANGED)

cv2.line(img, (0,0), (200,350), (0,0,0), 20)
cv2.rectangle(img, (150,50), (375,87) , (0,0,200), 8)
cv2.circle(img, (400,200), 75, (45,214,50), -1)

pts=np.array([[10,5],[20,56],[63,84],[98,75],[29,14],[58,32]],np.int32)
cv2.polylines(img, [pts], True, (200,200,200), 7)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Waterfall', (300,100), font, 2,(20,20,20), 3,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
