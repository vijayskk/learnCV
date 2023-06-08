import cv2.cv2 as cv2
import numpy as np
import time


cap = cv2.VideoCapture("traffic.mp4",)

prev_frame_time = 0
new_frame_time = 0

w = cap.get(3)
h = cap.get(4)
while True:
    ret, frame = cap.read()

    if ret:

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cc  = cv2.CascadeClassifier("haarcascade_car.xml")
        cars = cc.detectMultiScale(frame,scaleFactor=1.09,minNeighbors=5)
        for (x,y,w,h) in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,100),2)

        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        fps = str(int(fps))
        cv2.putText(frame, f"Fps: {fps}", (7, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow('Video', frame)

    else:
        print('no video')
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

# press escape to exit
    if (cv2.waitKey(1) == 27):
       break
cap.release()
cv2.destroyAllWindows()