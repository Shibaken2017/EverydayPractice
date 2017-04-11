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
        self.initial()

        for i in range(N):
            self.recalc()


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

    def set_inital_kluster(self):
        '''
        初期の重心を決定する
        :return:
        '''
        #初期klusterをランダムサンプル
        tmp_list=random.sample(self.ele_list,self.K)
        i=0
        for ele in tmp_list:
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
        '''
        各elementと各kurlusterの距離を計算する
        :return:
        '''
        for i in range(len(self.ele_list)):
            self.calc_distance(i)

    def delete_kulster_element(self):
        #クラスタの要素を消去
        for kluster in self.kluster_list:
            kluster.id_set=set()
    def choose_kluster_element(self):
        '''
        各クラスタの要素を保持する
        :return:
        '''
        for ele in self.ele_list:
            #print(ele.id)
            #print(ele.choose_kluster())
            self.kluster_list[ele.choose_kluster()].add(ele.id)

    def reclac_klusters_position(self):
        '''
        各クラスタの重心を再計算
        :return:
        '''
        #    def recalc_position(self,ele_list):

        for kluster in self.kluster_list:
            kluster.recalc_position(self.ele_list)

    def initial(self):
        '''
        初回の計算
        :return:
        '''

        self.load_file(self.fname)
        self.set_inital_kluster()
        self.calc_distances()
        #ここまでok
        self.choose_kluster_element()

    def recalc(self):
        '''
        2回目以降の計算
        :return:
        '''
        #重心の再計算
        self.reclac_klusters_position()
        #重心との距離を計算
        self.calc_distances()

        #各クラスタの要素を決定
        self.delete_kulster_element()
        self.choose_kluster_element()




if __name__=='__main__':
    k=K_means("test.txt")
    a=(k.kluster_list[0].id_set)
    b=(k.kluster_list[1].id_set)
    print(a.intersection(b))


    #k.initial()
    #klusterとの距離が計算されているかの確認用
    #for i in range(len(k.ele_list)):
    #   print(k.ele_list[i].distance_dict)
    #print(k.kluster_list[0].id_set)
   # print(k.kluster_list[1].id_set)
