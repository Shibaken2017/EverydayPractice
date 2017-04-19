#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class MakeTestData:
    def __init__(self,N,k):
        '''
        :param N:サンプル数
        :param k: 特徴量の次元数
         '''
        self.N = N
        self.k = k

    def get_line(self):
        '''
        1element分の名前,特徴量を出力
        :return:
        '''
        source_str = 'abcdefghijklmnopqrstuvwxyz'
        random.choice(source_str)  # a〜zでランダムに１文字
        random_str="".join([random.choice(source_str) for x in range(10)])
        line=random_str
        for i in range(self.k):
            line+='\t'+str(random.random())
        return line+'\n'

    def write_txt(self,fname):
        with open( fname,"w")as writer:
            for i in range(self.N):
                writer.write(self.get_line().encode('utf8','ignore'))





if __name__ == '__main__':
    test=MakeTestData(600,4)
    test.write_txt("test.txt")

