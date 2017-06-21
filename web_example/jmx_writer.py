#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et
import os

'''
入力ファイルにNこのテストプランがあるときか、次書の処理を行う
for i=0~N
    ・i個目のテストプランのみを有効
    ・ファイルに保存
'''

class JmxWriter:
    def __init__(self,num_of_users_list=[1,8,16,32,64,128]):
        print "nyan"
        self.__num_of_users_list=num_of_users_list

    def exe(self,input_jmx_file,output_dir="./"):
        '''

        :param input_jmx_file:
        :param output_dir:
        :return:
        '''
        self.__output_dir=output_dir
        self.load(input_jmx_file)
        self.count_num_of_testplans()
        self.write_plans()


    def load(self,input_jmx_file):
        if not os.path.exists(input_jmx_file):
            raise Exception(input_jmx_file+"は存在しません")
        self.tree = et.parse(input_jmx_file)
        self.root = self.tree.getroot()
        #self.count_num_of_testplans()

    def write_plans(self):
        for i in range(self.__num_of_plans):
            print i
            for num in self.__num_of_users_list:
                self.write_one_plan(i,num)

    def count_num_of_testplans(self):
        self.__num_of_plans=0

        for neighbor in self.root.iter('kg.apc.jmeter.timers.VariableThroughputTimer'):

            #print(neighbor.attrib["enabled"])
            self.__num_of_plans+=1


    def rewrite_num_of_users(self,num):

        for ele in self.root.iter("stringProp"):
            if ele.attrib["name"] == "ThreadGroup.num_threads":
                ele.text=str(num)
                print  ele.text
                ele.set('updated', 'yes')

                break


        print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

        for neighbor in self.root.findall("stringProp"):
            print neighbor.attrib


    def write_one_plan(self,num,num_of_users=8):
        '''

        (1)指定されたテストプランのみ有効
        (2)指定されたーユー０ザー数に設定
        :param num:テストプランの番号：
        :param num_of_users: ユーザー数
        :return:
        '''
        '''
        
        :param num: 
        :param users: 
        :return: 
        '''



        output_fname=""
        i=0
        for neighbor in self.root.iter('kg.apc.jmeter.timers.VariableThroughputTimer'):
            if i==num:
                #print neighbor.attrib
                output_fname+=str(num_of_users)+"users_"+neighbor.attrib["testname"]
                neighbor.attrib["enabled"]="true"
                neighbor.set('updated', 'yes')

            else:
                neighbor.attrib["enabled"]="false"
                neighbor.set('updated', 'yes')

            i+=1
        print output_fname
        self.rewrite_num_of_users(num_of_users)
        #xml保存
        self.tree.write(self.__output_dir+output_fname+".jmx")

if __name__=="__main__":
    test=JmxWriter()
    #test.exe("hello_world.jmx","/home/shib/IDE_etc/apache-jmeter-3.2/bin/jmx_files/")
