'''
K_means法の実装。各クラスターの重心の情報を保持する
'''

import numpy as np

class Gravity:
    def __init__(self,position,id):
        '''
        :param position: 重心の位置ベクトル
        :param id: 重心のid
        '''
        self.gravity_id=id
        self.position=position
        #クラスターに属する要素のidを保持
        self.id_set=set()



    def add(self,id):
        self.id_set.add(id)
    def initialize(self):
        '''
        集合を初期化する
        :return:
        '''
        self.id_set=set()



if __name__=='__main__':
    gravity=Gravity([1,2,3],2)
    gravity.add(2)
    gravity.add(3)
    print(gravity.id_set)



