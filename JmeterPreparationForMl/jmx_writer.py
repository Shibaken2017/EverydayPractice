#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et
import os
import shutil
'''
入力ファイルにNこのテストプランがあるときか、次の処理を行う
for i=0~N
    ・i個目のテストプランのみを有効
    ・ファイルに保存
'''

class JmxWriter:
    def __init__(self):
        print "nyan"



    def clean_dir(self,target_dir):
        '''
        target_dir内にあるフォルダ及びファイルを全削除
        :param target_dir:
        :return:
        '''
        if not os.path.exists(target_dir):
            raise Exception("dirがありませｎ!")
        fold_list = os.listdir(target_dir)
        #print fold_list
        for fold in fold_list:
            name=os.path.join(target_dir, fold)
            if os.path.isdir(name):
                shutil.rmtree(os.path.join(target_dir, fold))
            else:
                os.remove(name)

    def __clean_dir(self):
        '''
        出力dirを一旦空にする
        :return:
        '''
        fold_list = os.listdir(self.__output_dir)
        for fold in fold_list:
            shutil.rmtree(os.path.join(self.__output_dir, fold))







    def exe(self,input_jmx_file,num_of_users,output_dir="./"):
        '''
        input_jmx_fileを指定したユーザー数に回帰変える
        :param input_jmx_file:
        :param output_dir:
        :return:
        '''
        self.__num_of_users=num_of_users
        self.__output_dir=output_dir
        if not os.path.exists(self.__output_dir):
            raise Exception("dirがありませｎ")
        ##self.__clean_dir()


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
            self.write_one_plan(i,self.__num_of_users)

    def count_num_of_testplans(self):
        self.__num_of_plans=0

        for neighbor in self.root.iter('kg.apc.jmeter.timers.VariableThroughputTimer'):

            #print(neighbor.attrib["enabled"])
            self.__num_of_plans+=1
        print "test planの数"
        print self.__num_of_plans


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


    def write_one_plan(self,num,num_of_users):
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
        self.tree.write(os.path.join(self.__output_dir,output_fname+".jmx"))

if __name__=="__main__":
    RPS=["1_50","50_100","100_200"]



    output_base_dir="/home/shibaken/IDEetc/apache-jmeter-3.2/bin/jmx_files/ml_eco/"
    test=JmxWriter()
    test.clean_dir(output_base_dir)

    for user in [1,2,4,8,16]:
        output_dir=output_base_dir
        test.exe("./jmx_files/reciver_test.jmx",user,output_dir)



    #rps
    '''for rps in RPS:

        #user数
        for i in [8,16,32,64,128]:

            output_dir=os.path.join(output_base_dir,"{}RPS".format(rps),"{}users".format(i))
            os.makedirs(output_dir)
            test.exe("./jmx_files/hello_world_sleep/{}RPS.jmx".format(rps),i
                     ,output_dir)
    '''