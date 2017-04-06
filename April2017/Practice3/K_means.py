'''
K_means法の実装
'''
import numpy as np
from April2017.Practice3 import Element
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

class K_means:
    def __init__(self,fname,K=3,N=100):
        '''
        :param fname:
        :param K:クラ―スター数
        :param N: 反復回数
        '''
        self.ele_list=[]
        self.load_file(fname)


    def load_file(self,fname):
        with open(fname,"r",encoding="UTF-8")as reader:
            i=0
            for line in reader:
                tmp=line.strip().split("\t")
                id=i
                name=tmp[0]
                #要素の位置ベクトル
                position=self.get_nparray(tmp[1:])
                self.ele_list.append(Element.Element(id,name,position))
                i+=1



    def get_nparray(self,list):
        '''
        ["1","2.2"]のような文字列配列をnp配列に変換
        :param list
        :return:
        '''
        tmp_list=[]
        for i in range(len(list)):
            tmp_list.append(float(list[i]))
        return np.array(tmp_list)



if __name__=='__main__':
    k=K_means("test.txt")
    print(k.ele_list[2])


