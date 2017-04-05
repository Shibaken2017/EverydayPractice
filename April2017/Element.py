'''
K_measn法の実装。
各要素の特徴ベクトル、名前、一意に識別するためのidを保持するためのクラス
'''
import numpy as np
import math
class ELement:
    def __init__(self,id,name,x):
        self.id=id
        self.name=name
        self.x=x
        #各重心と自身の距離を保持
        self.distance_dict={}

    def calc_distance(self,name,g):
        '''
        指定した重心との距離を測りdictに保存
        :param name:
        :param g:
        :return:
        '''
        self.distance_dict[name]=math.sqrt(np.dot(self.x-g,self.x-g))