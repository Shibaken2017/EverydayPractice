'''
K_means法の実装
'''
import numpy as np
from April2017.Practice3 import Element
import logging
import random
from April2017.Practice3 import Kluster


logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')

class K_means:
    def __init__(self,fname,K=3,N=100):
        '''
        :param fname:
        :param K:クラ―スター数
        :param N: 反復回数
        '''
        self.K=K
        self.N=N
        self.ele_list=[]
        self.kluster_list=[]
        self.fname=fname

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

    def set_inital_gravity(self):
        '''
        初期の重心を決定する
        :return:
        '''
        tmp_list=random.sample(self.ele_list,self.K)
        for ele in tmp_list:
            i=0
            #    def __init__(self,position,id):
            self.kluster_list.append(Kluster.Kluster(ele.position, i))
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

    def calc_distance(self,index):
        '''

        :param index:
        :return:
        '''
        for kluster in self.kluster_list:
            self.ele_list[index].calc_distance(kluster)

    def calc_distances(self):
        for i in range(len(self.ele_list)):
            self.calc_distance(i)

    def choose_kluster_element(self):
        '''
        各クラスタの要素を保持する
        :return:
        '''
        for ele in self.ele_list:
            self.kluster_list[ele.choose_kluster()].add(ele.id)



    def initial(self):
        '''
        初回の計算
        :return:
        '''
        self.load_file(self.fname)
        self.set_inital_gravity()
        self.calc_distances()
        self.choose_kluster_element()

if __name__=='__main__':
    k=K_means("test.txt")
    print(k.initial())
    print(k.kluster_list[0].id_set)

