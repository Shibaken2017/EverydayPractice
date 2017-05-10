#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np



face_img=cv2.imread("image/test3.jpg")
#rows,cols=img.shape[:2

nose_cascade=cv2.CascadeClassifier("conf/haarcascade_mcs_nose.xml")

gray=cv2.cvtColor(face_img,cv2.COLOR_BGR2GRAY)

nose_rects=nose_cascade.detectMultiScale(gray,1.3,5)

for(x,y,w,h)in nose_rects:
    cv2.rectangle(face_img,(x,y),(x+w,y+h),(0,255,0),1)

#cv2.imwrite("output/test8_3.jpg",face_img)
cv2.imwrite("output/test9.jpg",face_img)