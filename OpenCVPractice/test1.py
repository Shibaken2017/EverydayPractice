#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import cv2
img=cv2.imread('./image/test.jpg')
#opencv uses numpy data structure
print type(img)




gray_imag=cv2.imread("./image/test.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("output/test1.jpg",gray_imag)





print [x for x in dir(cv2)if x.startswith("COLOR_")]
yuv_imjg=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
#save each chanel
for i in range(3):
    cv2.imwrite("output/test2_"+str(i)+".jpg",yuv_imjg[:,:,i])