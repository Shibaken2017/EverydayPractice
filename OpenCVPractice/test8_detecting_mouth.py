#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np



face_img=cv2.imread("image/test3.jpg")
#rows,cols=img.shape[:2]
face_cascade=cv2.CascadeClassifier("./conf/haarcascade_frontalface_alt.xml")
#eye_cacade=cv2.CascadeClassifier("./conf/haarcascade_eye.xml")
mouth_cascade=cv2.CascadeClassifier("./conf/haarcascade_mcs_mouth.xml")

scaling_factor=0.5
gray=cv2.cvtColor(face_img,cv2.COLOR_BGR2GRAY)
#yuv_imjg=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
mouth_rects=mouth_cascade.detectMultiScale(gray,1.7,11)

for(x,y,w,h) in mouth_rects:
    y=int(y-0.15*h)
    cv2.rectangle(face_img,(x,y),(x+w,y+h),(120,120,0),3)

#    cv2.imwrite("output/test7_2.jpg",face_img)
cv2.imwrite("output/test8_3.jpg",face_img)