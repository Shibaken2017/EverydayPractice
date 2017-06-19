#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
SSH="aiueo"


class ShellWriter:
    '''
    複数のjmxファイルを実行するためのシェルスクリぷとを書き出すこ＾ーど０
    各テストごとにsleep時間を入れる

    '''
    def __init__(self,sleep_time=420,
                 process_list=[1,2,3],
                 connection_list=[1,8,16,32,64,128,256]
                 ):
        '''

        :param log_dir:
        :param sleep_time:
        :param process_list: nginx設定
        :param connection_list: nginx設定
        '''
        self.__process_list=process_list

        self.__connection_list=connection_list
        self.sleep_time=sleep_time
        print "nyan"


    def make_report_sub_dir(self,process,connection,jmx_base):
        '''

        :param connection:
        :param process:
        :param jmx_base:
        :return:
        '''

        self.__base_name="process{}_connection{}_{}".format(process,connection,jmx_base)

        self.__report_subdir_name=self.__report_dir+"/process{}_connection{}_{}/".format(process,connection,jmx_base)

        if not os.path.exists(self.__report_subdir_name):
            os.mkdir(self.__report_subdir_name)









    def initial_setting(self,jmx_files_dir,log_dir,report_dir):
        '''
        dir有無確認やdirの作成をする
        :return:
        '''

        if not os.path.exists(jmx_files_dir):
            raise Exception(jmx_files_dir + "は存在しません")
        self.__jmeter_fnames_list=os.listdir(jmx_files_dir)


        self.__jmx_files_dir = jmx_files_dir
        self.__log_dir = log_dir
        self.__report_dir = report_dir


        #report_dir.log_dirを作成する

        if not os.path.exists(self.__log_dir):
            print "log_dir作成"
            os.makedirs(self.__log_dir)

        if not os.path.exists(self.__report_dir):
            print "report_dir作成"
            os.makedirs(self.__report_dir)









    def exe(self,jmx_files_dir,log_dir,report_dir,output_fname):
        '''

        :param jmx_files_dir:
        :param log_dir:
        :param report_dir:
        :param output_fname:
        :return:
        '''
        self.output_txt=""
        self.initial_setting(jmx_files_dir,log_dir,report_dir)


        #jmeterの書き込み
        for process in self.__process_list:
            for connection in self.__connection_list:
                for fname in self.__jmeter_fnames_list:
                    self.make_report_sub_dir(process,connection,fname.split(".")[0])
                    self.write_jmeter_part(jmx_files_dir+fname)



        #ファイル出力
        with open(output_fname,"w")as writer:
            writer.write(self.output_txt)







    def write_line(self):

        line="jmeter -n -t my_test.jmx -l log.jtl -e -o report"


    def write_nginx_part(self,process,connection):
        '''
        ngnx設定部分を記述
        :return:
        '''
        #ssh接続
        self.output_txt+="ssh {}\n".format(SSH)

        #copy
        conf="process{}_connection{}.conf".format(process,connection)
        self.output_txt+="sudo cp  {} {}\n".format(conf,"/etc/nginx/nginx.conf")

        #nginx reload
        self.output_txt+="sudo nginx -s reload\n"
        #exit
        self.output_txt+="exit\n"




    def write_jmeter_part(self,jmx_fname):
        '''
        jmeter実行部分を記述
        :param jmx_fname:
        :param log_fname:
        :param report_dir_name:
        :return:
        '''

        log_name=self.__log_dir+self.__base_name+".jtl"
        #jmeter　実行部分の文字列を返す
        line="jmeter -n -t {} -l {} -e -o {}".format(jmx_fname,log_name,self.__report_subdir_name)
        self.output_txt+=line+"\n"
        self.output_txt+="sleep "+str(self.sleep_time)+"\n"



if __name__=="__main__":
    test=ShellWriter()
    test.exe("./jmx_files/","./logdir/","./report_dir/","test.sh","")
    #test.make_report_sub_dir(12,23,"test123")