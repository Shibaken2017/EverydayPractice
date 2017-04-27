#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append("./images")
sys.path.append(os.pardir)
import DlibPractice.face_utils as utils
import numpy as np
import argparse
import imutils
import dlib
import cv2



#python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/example_01.jpg
ap=argparse.ArgumentParser()
# construct the argument parser and parse the arguments
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
#引数の設定
args = vars(ap.parse_args())

#顔認識のためのobject
detector=dlib.get_frontal_face_detector()
#landmark識別のためのobject
predictor=dlib.shape_predictor(args["shape_predictor"])

#画像オブジェクト
image=cv2.imread(args["image"])
#size変換
image=imutils.resize(image,width=500)
#変換
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#顔識別の結
rects=detector(gray,1)

# loop over the face detections
#顔認識で見つかった書く顔についてlandmark_detect
for (i, rect) in enumerate(rects):
    # determine the facial landmarks for the face region, then
    # convert the facial landmark (x, y)-coordinates to a NumPy
    # array
    shape = predictor(gray, rect)
    #landmarksのnp配列を保存
    shape = utils.shape_to_np(shape)

    # convert dlib's rectangle to a OpenCV-style bounding box
    # [i.e., (x, y, w, h)], then draw the face bounding box
    (x, y, w, h) = utils.rect_to_bb(rect)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # show the face number
    cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # loop over the (x, y)-coordinates for the facial landmarks
    # and draw them on the image
    for (x, y) in shape:
        cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

# show the output image with the face detections + facial landmarks
#cv2.imshow("Output", image)
#cv2.waitKey(0)
cv2.imwrite("test.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, 100])