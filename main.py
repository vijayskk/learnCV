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

xx = 0
yy = 100
zz = 255
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    og = frame
    canvas = np.zeros(frame.shape,np.uint8)
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    _ , frame = cv2.threshold(frame,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    c,h = cv2.findContours(frame,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(canvas,c,-1,(0,255,100),2)
    cv2.imshow('webcam', cv2.add(og,canvas))
# press escape to exit
    if (cv2.waitKey(1) == 27):
       break
cap.release()
cv2.destroyAllWindows()