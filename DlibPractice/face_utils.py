#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
顔のパーツを認識するための   
'''
import numpy as np


def rect_to_bb(rect):
    '''
    画像の左端、上、幅、高さを返す、
    dlibではこの4つを返すのが慣習
    :param rect: 
    :return: 
    '''


    # take a bounding predicted by dlib and convert it
    # to the format (x, y, w, h) as we would normally do
    # with OpenCV
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y

    # return a tuple of (x, y, w, h)
    return (x, y, w, h)


def shape_to_np(shape, dtype="int"):
    '''
    detectorが返すshapeオブジェクトを配列に帰る
    :param shape: 
    :param dtype: 
    :return: 
    '''
    # initialize the list of (x, y)-coordinates
    coords = np.zeros((68, 2), dtype=dtype)

    # loop over the 68 facial landmarks and convert them
    # to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    # return the list of (x, y)-coordinates
    return coords






