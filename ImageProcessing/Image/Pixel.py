#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
各画素の情報をも保持するクラス
'''

class Pixel:
    def __init__(self,position,blue,red,green):
        '''
        
        :param position: 
        :type blue : int
        :param blue:
        :type red : int
        :param red: 
        :type green : int
        :param green: 
        '''
        self.position=position
        self.blue=blue
        self.red=red
        self.green=green

    def __str__(self):
        return str(self.position)+"\t"+"blue:"+str(self.blue)+"\t"+"red:"+str(self.red)+"\t"+"green:"+str(self.green)




