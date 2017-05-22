#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import numpy as np
#binary
#linear binary cllasification
class LinearClassifier:
    def __init__(self,fname):
        self.load_data(fname)


    def load_data(self,fname):
        with open(fname,"r")as reader:
            self.matrix_list=[]
            tmp_matrix=[]
            for line in reader:
                if line.startswith("group_id"):
                    tmp_matrix=[]
                elif len(line.strip())>0:
                    tmp_matrix.append(self.make_float_list(line.strip().split("\t")[1:]))
                else:
                    if len(tmp_matrix)>0:
                        self.matrix_list.append(tmp_matrix)
                        tmp_matrix=[]

    def make_float_list(self,input_list):
        '''
        ["1","1","3"]→[1,2,3]
        :param list: 
        :return: 
        '''
        output_list=[]
        for ele in input_list:
            output_list.append(float(ele))

        return output_list

    def make_cov_matrix(self):
        #calc cov matirxes
        tmp_cov_list=[]
        for mat in self.matrix_list:

            tmp_cov_list.append(np.cov(mat, rowvar=0, bias=1))
        print tmp_cov_list


if __name__ == '__main__':
    test=LinearClassifier("test.txt")
    print len(test.matrix_list)
    test.make_cov_matrix()


