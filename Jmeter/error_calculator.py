#!/usr/bin/env python
# -*- coding: utf-8 -*-
import  json
import os




class ErrorCalculator:
    def __init__(self):
        print "nyan"
        self.element_dict={}
        #toalの件数
        self.total=0
        #errorが起きた件数
        self.error=0
    def get_error(self, fname):
        with open(fname, "r")as reader:
            tmp = ""
            x = False
            for line in reader:
                if line.__contains__("createTable($(\"#statisticsTable\")"):
                    tmp += line
                    break

        return tmp.split(",")[5].strip()

    def extract_error_type(self,fname):
        '''
          jmeterをshellで実行した時のerror_typeごとの特徴を取り出す
          :param fname:
          :return:
          '''
        if float(self.get_error(fname))>0:
            self.error+=1

            with open(fname, "r") as reader:
                tmp = ""
                x = False
                for line in reader:
                    if line.__contains__(r'createTable($("#errorsTable")'):
                        tmp += line
                        #print tmp
                        break

            tmp = tmp.split(",", 1)[1]
            tmp = tmp.rsplit(",", 2)[0]
            error_json= json.loads(tmp)
            for item in error_json["items"]:
                item=item["data"]
                #print item[0]
                #if item[0].__contains__("Network is unreachable"):
                   # print fname
                self.element_dict.setdefault(item[0],Element(item[0]))
                self.element_dict[item[0]].count+=1
                self.element_dict[item[0]].error_sum+=item[3]
                self.element_dict[item[0]].id_set.add(self.total)



    def summarize_error_count(self):
        for ele in self.element_dict.values():
            ele.error_rate=ele.error_sum/ele.count
            print "{}:error_rate{}頻度{}".format(ele.error_type,ele.error_rate,float(ele.count)/float(self.error))




    def exe(self,target_dir):
        folders=os.listdir(target_dir)
        num=0
        for folder in folders:
            num+=1
            #print num
            fname=os.path.join(target_dir,folder,"content","js","dashboard.js")
            if os.path.exists(fname):
                self.total+=1
                self.extract_error_type(fname)







class Element:
    def __init__(self,error_type):
        self.error_type=error_type
        self.count=0
        self.error_sum=0
        self.error_rate=0
        self.id_set=set()



if __name__=="__main__":
    test=ErrorCalculator()
    #test.extract_error_type("/home/shibaken/IDEetc/"
      #             "apache-jmeter-3.2/bin/hello_world_sleep/process1_connection128_64users_100_200RPS_s3"
       #            "/content/js/dashboard.js")

    #test.extract_error_type("/home/shibaken/IDEetc/apache-jmeter-3.2/bin/hello_world_sleep/process1_connection16_8users_100_200RPS_s3/content/js"
     #                       "/dashboard.js")

    test.exe("/home/shibaken/IDEetc/apache-jmeter-3.2/bin/hello_world_sleep/")

    test.summarize_error_count()

    print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    keys=test.element_dict.keys()
    print keys
    print len(keys)
    print test.total
    print test.error