'''
ウァード法によるアルゴリズム
'''
import numpy as np
from April2017.Practice4.Element import Element
from April2017.Practice4.Kluster import Kluster
class Ward:
    def __init__(self,fname):
        self.ele_list=[]
        #key:id,value:element class
        self.kluster_dict={}
        self.load_file()


    def load_file(self,fname):
        with open(fname,"r",encoding="UTF-8")as reader:
            i=0
            for line in reader:
                tmp=line.strip().split("\t")
                id=i
                name=tmp[0]
                #要素の位置ベクトル
                position=self.get_nparray(tmp[1:])
                self.ele_list.append(Element(id,name,position))
                i+=1

    def get_nparray(self, list):
        '''
        ["1","2.2"]のような文字列配列をnp配列に変換
        :param list
        :return:
        '''
        tmp_list = []
        for i in range(len(list)):
            tmp_list.append(float(list[i]))
        return np.array(tmp_list)



    def merge_kluster(self,kluster1,kluster2):
        '''
        :type kluster1: Kluster
        :param kluster1:
        :type kluster2: Kluster
        :param kluster2:
        :return:
        '''
        #大きいidを削除する
        new_id=min(kluster1.id,kluster2.id)
        delete_id=max(kluster1.id,kluster2,id)
        self.kluster_dict[new_id].add_elements(self.kluster_dict[delete_id].ele_list)

        del self.kluster_dict[delete_id]