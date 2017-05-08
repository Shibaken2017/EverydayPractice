#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
img=cv2.imread("image/test.jpg")
num_rows,num_cols=img.shape[:2]


print img.shape

rotation_matrix=cv2.getRotationMatrix2D((num_cols/2,num_rows/2),30,1)


print rotation_matrix