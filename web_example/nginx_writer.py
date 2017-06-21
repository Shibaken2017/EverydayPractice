#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
class NginxWriter:
    '''
    指定したプロセス数。・コネックション数のnginxファイルを位描き上げる
    '''
    def __init__(self,    process_list=[1,2,3],
                 connection_list=[1,8,16,32,64,128,256]):
        print "nyan"
        self.__process_list=process_list=process_list
        self.__connection_list=connection_list=connection_list

    def rewrite_all(self,fname,output_dir="./"):
        self.__output_dir=output_dir
        for process in self.__process_list:
            for connection in self.__connection_list:
                self.rewrite(fname,process,connection)


    def rewrite(self,fname,process,connection):
        output_txt=""
        with open(fname,"r")as reader:
            for line in reader:
                if line.__contains__("worker_processes"):
                    output_txt+="worker_processes {};\n".format(process)

                elif line.__contains__("worker_connections"):
                    output_txt+="worker_connections {}:\n".format(connection)

                else:
                    output_txt+=line
        output_fname="process{}_connection{}.conf".format(process,connection)
        with open(self.__output_dir+output_fname,"w")as writer:
            writer.write(output_txt)

if __name__=="__main__":
    test=NginxWriter()
    test.rewrite_all("nginx.conf","./nginx_files/")



