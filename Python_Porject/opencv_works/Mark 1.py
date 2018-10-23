import cv2 as cv
import numpy as np

img = cv.imread('image1.png',0)
cv.imshow('image',img)
k = cv.waitKey(0)

if k == ord('q'):
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('image2.png',img)
    cv.destroyAllWindows()