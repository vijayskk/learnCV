import cv2.cv2 as cv2
import numpy as np



cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    fc  = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    ec = cv2.CascadeClassifier("haarcascade_eye.xml")
    faces = fc.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    eyes = ec.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,100),2)

    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,100),2)

    cv2.imshow('webcam', frame)
# press escape to exit
    if (cv2.waitKey(1) == 27):
       break
cap.release()
cv2.destroyAllWindows()