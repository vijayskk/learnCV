import cv2.cv2 as cv2
import math

import numpy as np


def makeBit(img,thresh=255/2):
    inxi = 0
    for i in img:
        inxj = 0
        for j in i:
            if j >= thresh:
                img[inxi][inxj] = 255
            else:
                img[inxi][inxj] = 0

            inxj+=1
        inxi+=1
    return img

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)

    hc = cv2.cornerHarris(gray,3,3,.05)

    kernel = np.ones((7,7),np.uint8)
    hc = cv2.dilate(hc,kernel,iterations=2)
    frame[hc>0.025*hc.max()] = [0,255,100]
    cv2.imshow('webcam', frame)
# press escape to exit
    if (cv2.waitKey(1) == 27):
       break
cap.release()
cv2.destroyAllWindows()