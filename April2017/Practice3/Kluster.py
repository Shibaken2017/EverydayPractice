'''
K_means法の実装。各クラスターの重心の情報を保持する
'''

import numpy as np

class Kluster:
    def __init__(self,position,id):
        '''
        :param position: 重心の位置ベクトル
        :param id: 重心のid
        '''
        self.id=id
        self.position=position
        #クラスターに属する要素のidを保持
        self.id_set=set()



    def add(self,id):
        '''
        クラスターの要素を追加
        :param id:
        :return:
        '''
        self.id_set.add(id)
    def initialize(self):
        '''
        集合を初期化する
        :return:
        '''
        self.id_set=set()

    def recalc_position(self,ele_list):
        '''
        重心の再計算
        :param list:
        :return:
        '''
        sum=np.array([float(0) for i in range(len(self.position))])
        for id in self.id_set:
            sum+=ele_list[id].position


        self.position=sum/len(self.id_set)
        #print(self.position)



if __name__=='__main__':
    gravity=Kluster([1,2,3],2)
    gravity.add(2)
    gravity.add(3)
    print(gravity.id_set)



