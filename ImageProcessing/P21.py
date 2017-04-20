#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os import path
import sys
sys.path.append("./Image")
sys.path.append(os.pardir)

from ImageProcessing.Image.Picture import  Picture
from ImageProcessing.Image.Pixel import Pixel

'''
    B/G/Rのの入れ替えプログラム
'''
class ColorConverter:
    def __init__(self,picture):
        '''
        :type Picture : Picture
        :param Picture : 
        '''
        self.picture=picture

    def converte_all(self):
        '''
        apply exchange method to all pixels
        :return: 
        '''
        for i in range(self.picture.X):
            for j in range(self.picture.Y):
                self.convert(i,j)



    def convert(self,i,j):
        '''
        exchange colors at designated pixel
        :param i: 
        :param j: 
        :return: 
        '''
        tmp_blue=self.picture.pixel_list[i][j].blue
        tmp_red=self.picture.pixel_list[i][j].red
        tmp_green=self.picture.pixel_list[i][j].green

        self.picture.pixel_list[i][j].blue=tmp_green
        self.picture.pixel_list[i][j].green=tmp_red
        self.picture.pixel_list[i][j].red=tmp_blue










if __name__=='__main__':
    pix00=Pixel([0,0],122,110,90)
    pix01=Pixel([0,1],123,113,145)
    pix10=Pixel([1,0],222,123,122)
    pix11=Pixel([1,1],212,112,211)

    pic=Picture([[pix00,pix01],[pix10,pix11]])



    test=ColorConverter(pic)
    test.converte_all()
