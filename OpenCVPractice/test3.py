#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

#affine_transformation
img=cv2.imread("img/test.jpg")
rows,cols=img.shape[:2]
src_points=np.float32([[0,0],[cols-1,0],[0,rows-1]])


dist_points=np.float32([[0,0],[int(0.6*(cols-1)),0],[int(0.4*(cols-1)),rows-1]])
affine_matrix=cv2.getAffineTransform(src_points,dist_points)

img_output=cv2.warpAffine(img,affine_matrix,(cols,rows))
cv2.imwrite("output/test4.jpg",img_output)


