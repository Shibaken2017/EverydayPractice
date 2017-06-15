#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as et

'''
入力ファイルにNこのテストプランがあるときか、次書の処理を行う
for i=0~N
    ・i個目のテストプランのみを有効
    ・ファイルに保存
'''

class JmxWriter:
    def __init__(self):
        print "nyan"

    def exe(self,input_jmx_file,output_dir="./"):
        self.__output_dir=output_dir
        self.load(input_jmx_file)
        self.count_num_of_testplans()

        self.write_plans()


    def load(self,input_jmx_file):
        self.tree = et.parse(input_jmx_file)
        self.root = self.tree.getroot()
        #self.count_num_of_testplans()

    def write_plans(self):
        for i in range(self.__num_of_plans):
            print i
            self.write_one_plan(i)

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


    def write_one_plan(self,num,users=8):



        output_fname=""
        i=0
        for neighbor in self.root.iter('kg.apc.jmeter.timers.VariableThroughputTimer'):
            if i==num:
                #print neighbor.attrib
                output_fname+=neighbor.attrib["testname"]
                neighbor.attrib["enabled"]="true"
                neighbor.set('updated', 'yes')

            else:
                neighbor.attrib["enabled"]="false"
                neighbor.set('updated', 'yes')

            i+=1
        print output_fname
        self.rewrite_num_of_users(200)
        self.tree.write(self.__output_dir+output_fname+".jmx")

if __name__=="__main__":
    test=JmxWriter()
    test.exe("web_sdk_loading_test.jmx","jmx_files/")
    #test.rewrite_num_of_users()
    #tree = et.parse("web_sdk_loading_test.jmx")
   # root =tree.getroot()
    #for ele in  root.iter("stringProp"):
    #    if ele.attrib["name"]=="ThreadGroup.num_threads":
    #        print ele.text
    #        #print "aaaaaaaaaaaaaa"
        #print ele.text