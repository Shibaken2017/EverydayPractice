#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

img=cv2.imread("img/test2.jpg")
rows,cols=img.shape[:2]

#vignette mask using

kernel_x=cv2.getGaussianKernel(cols,200)
kernel_y=cv2.getGaussianKernel(rows,200)
kernel=kernel_y*kernel_x.T
mask=255*kernel/np.linalg.norm(kernel)
output=np.copy(img)

for i in range(3):
    output[:,:,i]=output[:,:,i]*mask


cv2.imwrite("output/vignet.jpg",output)

