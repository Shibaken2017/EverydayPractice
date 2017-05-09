#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np



#low pass filter

img=cv2.imread("img/test2.jpg")
rows,cols=img.shape[:2]
kernel_identity=np.array([[0,0,0],[0,1,0],[0,0,0]])
kernel_3x3=np.ones((3,3),np.float)/9.0
output=cv2.filter2D(img,-1,kernel_identity)
cv2.imwrite("output/test5.jpg",output)


output=cv2.filter2D(img,-1,kernel_3x3)
cv2.imwrite("output/test6.jpg",output)


##########################################
#edge detection
#rows,cols=img.shape

sobel_horizontal=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_vertical=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imwrite("output/sobel_horizontal.jpg",sobel_horizontal)
cv2.imwrite("output/sobel_vertial.jpg",sobel_vertical)



#laplacian filter
lap=cv2.Laplacian(img,cv2.CV_64F)

cv2.imwrite("output/lap.jpg",lap)


#erosion
kernel=np.ones((5,5),np.float32)

img_erosion=cv2.erode(img,kernel,iterations=1)
img_dilation=cv2.dilate(img,kernel,iterations=1)
cv2.imwrite("output/erosion.jpg",img_erosion)
cv2.imwrite("output/dilation.jpg",img_dilation)

