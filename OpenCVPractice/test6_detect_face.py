#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np




face_img=cv2.imread("image/test.jpg")
#rows,cols=img.shape[:2]
face_cascade=cv2.CascadeClassifier("./conf/haarcascade_frontalface_alt.xml")

scaling_factor=0.5
gray=cv2.cvtColor(face_img,cv2.COLOR_BGR2GRAY)
#yuv_imjg=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
face_rects=face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in face_rects:
    cv2.rectangle(face_img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imwrite("output/test6.jpg",face_img)

