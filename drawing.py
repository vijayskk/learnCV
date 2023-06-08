import cv2.cv2 as cv2
import numpy as np
from tkinter import *
canvas = np.zeros((512,512,3),np.uint8)




def drawRect(x,y,w,h,title):
    cv2.putText(canvas,title,(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
    cv2.line(canvas, (x, y), (x+w, y), (255, 0, 0), 5)
    cv2.line(canvas, (x, y), (x, y+h), (255, 0, 0), 5)
    cv2.line(canvas, (x, y+h), (x+w, y+h), (255, 0, 0), 5)
    cv2.line(canvas, (x+w, y), (x+w, y+h), (255, 0, 0), 5)

drawRect(50,50,50,100,"Found")

cv2.imshow("Canvas",canvas)

cv2.waitKey(0)
mainloop()
