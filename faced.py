#!/usr/bin/python

import numpy as np
import cv2 as cv
import os, sys
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
img = cv.imread('face3.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
x=0

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        x=1

if x==1:
	y=1
else:
	y=0
	
print(y)
os.makedirs("ass");
# cv.imshow('img',img)
# cv.resizeWindow('img', 200,200)
# cv.waitKey(0)
# cv.destroyAllWindows()