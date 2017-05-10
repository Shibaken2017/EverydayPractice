#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np





face_img=cv2.imread("image/test3.jpg")
#rows,cols=img.shape[:2]
face_cascade=cv2.CascadeClassifier("./conf/haarcascade_frontalface_alt.xml")
eye_cacade=cv2.CascadeClassifier("./conf/haarcascade_eye.xml")

scaling_factor=0.5
gray=cv2.cvtColor(face_img,cv2.COLOR_BGR2GRAY)
#yuv_imjg=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
face_rects=face_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in face_rects:
    roi_gray=gray[y:y+h,x:x+w]
    roi_color=face_img[y:y+h,x:x+w]
    #cv2.rectangle(face_img,(x,y),(x+w,y+h),(0,255,0),3)
    eyes=eye_cacade.detectMultiScale(roi_gray)
    for (x_eye,y_eye,w_eye,h_eye)in eyes:
        center=(int(x_eye+0.5*w_eye),int(y_eye+0.5*h_eye))
        radius=int(0.3*(w_eye+h_eye))
        color=(0,255,0)
        thickness=1
        cv2.circle(roi_color,center,radius,color,thickness)
    cv2.imwrite("output/test7_2.jpg",face_img)

#cv2.imwrite("output/test6.jpg",face_img)

