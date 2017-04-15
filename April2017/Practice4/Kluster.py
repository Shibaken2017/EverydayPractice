'''
各クラスタの要素等を保持する
ここでクラスタの散らばしの指標はtrを用いる
例えばクラスタw1,w2,w3取る時の散らばり具合はtrW１＋ｔｒＷ２+trW3 で定義する
'''
import numpy as np
from April2017.Practice4 import Element

class Kluster:

    def __init__(self,id,ele_list):
        '''
        :type id: int
        :param id:
        :type ele_list: list[ Element ]
        :param ele_list:
        '''
        '''

        :param id: クラスタid
        :param ele_set: elementのset

        '''

        if len(ele_list)==0 or ele_list==None:
            raise Exception("ele_listが空です")
        self.id=id
        self.ele_list=ele_list
        self.mean=None
        self.calc_tr()

    def calc_kluster_tr(self,kluster):
        '''
        kluster間の距離を測る
        :return:
        '''
        tmp_list=[]
        tmp_list.extend(self.ele_list)
        tmp_list.extend(kluster.ele_list)
        tmp_kluster=Kluster(float("inf"),tmp_list)
        tmp_kluster.calc_tr()
        return tmp_kluster.tr





    def calc_tr(self):
        '''
        self.ele_listを用いてtrを求める
        :return:
        '''
        self.calc_cov()
        self.tr=sum([self.cov[i][i]  for i in range((self.cov.shape[0]))])


    def calc_cov(self):
        '''
        共分散行列の計算
        :return:
        '''
        self.calc_mean()
        self.cov=np.dot(self.ele_list[0].position-self.mean,(self.ele_list[0].position-self.mean).T)
        if len(self.ele_list)>2:
            for i in range(2,len(self.ele_list)):
                self.cov+=np.dot(self.ele_list[i].position-self.mean,(self.ele_list[i].position-self.mean).T)




    def calc_mean(self):
        '''
        ele_listから平均ベクトルを求める
        :return:
        '''
        self.mean=self.ele_list[0].position
        if len(self.ele_list)>=2:
            for i in range(1,len(self.ele_list)):
                self.mean+=self.ele_list[i].position

        self.mean=self.mean/len(self.ele_list)
    def add_elements(self,element_list):
        '''
        クラスターにelementを足す
        :param element_list:
        :return:
        '''
        self.ele_list.extend(element_list)



    def __str__(self):
        tmp_list=[]
        for ele in self.ele_list:
            tmp_list.append(ele.id)

        output="Klu_id:{},ele_list:{}".format(self.id,tmp_list)
        return output







if __name__=='__main__':
    ele1=Element.Element(1,"shiba",np.array([[1],[2],[3],[4]]))
    ele2=Element.Element(2,"ken",np.array([[2],[3],[4],[54]]))

    element_list=[ele1,ele2]
    k=Kluster(1,element_list)
    print(k)
   # print(k.calc_kluster_tr(k))
    #k.calc_tr()
    #print(k.tr)

