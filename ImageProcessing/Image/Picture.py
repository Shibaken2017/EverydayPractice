#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
画像を表すクラス
'''
import os

import sys
sys.path.append("../../")
sys.path.append(os.pardir)
from ImageProcessing.Image.Pixel import  Pixel


class Picture:
    def __init__(self,pixel_list,id=None,name=None):

        self.pixel_list=pixel_list
        self.id=id
        self.name=name
        self.X=len(self.pixel_list)
        self.Y=len(self.pixel_list[0])


if __name__=='__main__':
    pix00=Pixel([0,0],122,110,90)
    pix01=Pixel([0,1],123,113,145)
    pix10=Pixel([1,0],222,123,122)
    pix11=Pixel([1,1],212,112,211)

    pic=Picture([[pix00,pix01],[pix10,pix11]])
    print pic.pixel_list[0][0]
    print pic.pixel_list[0][1]