#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import numpy as np

class MakeTestData:
    def __init__(self,N,k,num_of_group):
        '''
         ・create test data for linear classification
        ・data of each group is generated from normal distribution 
         :type N : int
        :param N: num of sample for each group
        :type k : int
        :param k: feature dimensions
        :type : int
        :param num_of_group:  
        '''

        self.N = N
        self.k = k
        self.num_of_group=num_of_group

    def get_line(self,mean,sd,id):
        '''
        get random number from normal distribution
        :return:
        '''
        line=str(id)
        for i in range(self.k):
            line+='\t'+str(np.random.normal(mean,sd))
        return line+'\n'

    def get_group(self,group_id,mean,sd):
        '''
        :type : int
        :param id: 
        :return: 
        '''
        return "group_id\t"+str(group_id)+"\tmean="+str(mean)+"\tsd="+str(sd)+"\n"


    def write_group(self,writer,id):
        '''
        
        :param writer: 
        :return: 
        '''
        mean=10*np.random.random()
        sd=10*np.random.random()
        writer.write(self.get_group(id,mean,sd))

        for id in range(self.N):
            writer.write(self.get_line(mean,sd,id))
        writer.write("\n")



    def write_txt(self,fname):
        with open( fname,"w")as writer:
            for group_id in range(self.num_of_group):
                self.write_group(writer,group_id)




if __name__ == '__main__':
    test=MakeTestData(100,4,2)
    test.write_txt("test.txt")

