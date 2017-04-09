'''
K_measn法の実装。
各要素の特徴ベクトル、名前、一意に識別するためのidを保持するためのクラス
'''
import numpy as np
import math

class Element:
    def __init__(self,id,name,position):
        '''

        :param id:
        :param name:
        :param position:t位置ベクトル
        '''
        self.id=id
        self.name=name
        self.position=position
        #key:各重心のid
        # valuer:その重心との距離
        self.distance_dict={}

    def calc_distance(self,kluster):
        '''
        指定した重心との距離を測りdictに保存
        :param name:
        :param kluster:
        :return:
        '''
        self.distance_dict[kluster.id]=math.sqrt(np.dot(self.position-kluster.position,self.position-kluster.position))

    def choose_kluster(self):

        '''
        どのklusterに属するかかを決める
        :return:
        '''
        tmp_id=0
        tmp_dist=0
        for id in self.distance_dict.keys():
            if tmp_dist<self.distance_dict[id]:
                tmp_id=id
                tmp_dist=self.distance_dict

            return tmp_id


