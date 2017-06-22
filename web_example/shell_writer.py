#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

SSH = "aiueo"


class ShellWriter:
    '''
    複数のjmxファイルを実行するためのシェルスクリぷとを書き出すこ＾ーど０
    各テストごとにsleep時間を入れる

    '''

    def __init__(self,ssh_file="./ssh.txt"):

        print "nyan"
        with open(ssh_file,"r")as reader:
            self.ssh=reader.read()




    def exe(self, jmx_dir, report_dir, log_dir, output_fname,sleep_time=420):
        '''
          :param jmx_dir:
          :param report_dir:
          :param log_dir:
          :return:
          '''
        self.__sleep_time=sleep_time

        self.__output_txt = ""
        self.__jmx_dir = jmx_dir
        self.__log_dir = log_dir
        self.__report_dir = report_dir
        self.write_initial_part()
        self.write_jmeter_part()
        with open(output_fname, "w")as writer:
            writer.write(self.__output_txt)

    def write_initial_part(self):


        self.__output_txt += "for process in 1 2 3;do\n"
        self.__output_txt += "for connection in 1 8 16 32 64 128 256;do\n"
        # ssh接続＆connetctionとprocess数変更
        self.__output_txt += "ssh  {} ".format(self.ssh)
        self.__output_txt += "sudo python /home/taro_biwajima/gitproject/Practice/web_example/nginx_rewriter.py /etc/nginx/nginx.conf ${process} ${connection}\n"
        #self.__output_txt+="exit\n"
    def write_jmeter_part(self):
        # jmeter -n -t my_test.jmx -l log.jtl -e -o report
        jmeter_fnames = os.listdir(self.__jmx_dir)

        for jmeter_fname in jmeter_fnames:
            report = self.__report_dir + "process${process}_connection${connection}_" \
                     + jmeter_fname.split(".")[0]

            log = self.__log_dir + "process${process}_connection${connection}_" \
                  + jmeter_fname.split(".")[0] + ".jtl"

            # base="process{}_connection{}_".format(process,connection)+fname.split(".")[0]
            self.__output_txt+="\tmkdir "+report+"\n"
            self.__output_txt += "\t./jmeter -n -t {} -l {} -e -o {}\n".format(self.__jmx_dir + jmeter_fname, log, report)
            self.__output_txt+="\tsleep {}\n".format(self.__sleep_time)

        self.__output_txt += "done\n"
        self.__output_txt+="done\n"

if __name__ == "__main__":
    writer = ShellWriter()
    #    def exe(self, jmx_dir, report_dir, log_dir, output_fname):

    writer.exe("/home/shibaken/IDEetc/apache-jmeter-3.2/bin/jmx_files/","/home/shibaken/IDEetc/apache-jmeter-3.2/bin/report_dir/",
               "/home/shibaken/IDEetc/apache-jmeter-3.2/bin/log_dir/","test.sh")
