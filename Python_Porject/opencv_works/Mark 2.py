import numpy as np 
import cv2 as cv 

cap = cv.VideoCapture(0)

while (True):
    ret,frame = cap.read()
    ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,640)
    ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,480)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destoryAllWindows()