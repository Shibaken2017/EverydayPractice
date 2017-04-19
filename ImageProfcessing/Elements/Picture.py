#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
画像を表すクラス
'''
from ImageProfcessing.Elements.Pixel import  Pixel
class Picture:
    def __init__(self,pixel_list,id=None,name=None):

        self.pixel_list=pixel_list
        self.id=id
        self.name=name


