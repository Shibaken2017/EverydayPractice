#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# SSH = "aiueo"

HOME_DIR = "~/IDEetc/apache-jmeter-3.2/bin"
#CONNECTIONS = [8, 16, 32, 64, 128, 256]
#PROCESS = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


class ShellWriter:
    '''
    複数のjmxファイルを実行するためのシェルスクリぷとを書き出すこ＾ーど０
    各テストごとにsleep時間を入れる

    '''

    def __init__(self):
        print "nyan"
        # with open(ssh_file,"r")as reader:
        #    self.ssh=reader.read()

    def exe(self, jmx_dir, report_dir, log_dir, output_shell_fname
            , time_limit=420, sleep_time=420, max_queue=1000, mode="w"):
        '''

        :param jmx_dir:
        :param report_dir:
        :param log_dir:
        :param output_shell_fname:
        :param time_limit: この秒数以内にテストが終わらなかったら失敗したとして終了する
        :param sleep_time: shファイルの名前
        :param max_queue:server側のパラメータ
        :param mode:
        :return:
        '''

        self.time_limit = time_limit
        self.__sleep_time = sleep_time
        self.max_queue = max_queue
        self.__output_txt = ""
        self.__jmx_dir = jmx_dir
        self.__log_dir = log_dir
        self.__report_dir = report_dir

        self.check_dirs()
        self.write_jmeter_part()
        print "書き込み中"
        with open(output_shell_fname, mode)as writer:
            writer.write("#warning:check wheter reciver is correctly configured \n")
            writer.write("cd {}n".format(HOME_DIR))

            writer.write(self.__output_txt)
        print "書き込み終了"

  #  def __write_process_line(self):
  #      output_txt = ""
  #      for pro in PROCESS:
  #          output_txt += str(pro) + " "
  #      return output_txt


    def check_dirs(self):
        '''
        logdir,resultdirがなかったら作成する
        :return:
        '''
        template="dir={}; [ ! -e $dir ] && mkdir -p $dir\n"
        self.__output_txt+="\n"
        self.__output_txt+="#check dirs\n"
        self.__output_txt+=template.format(self.__log_dir)
        self.__output_txt+=template.format(self.__report_dir)
        self.__output_txt+="\n"



    def write_jmeter_part(self):
        # jmeter -n -t my_test.jmx -l log.jtl -e -o report
        jmeter_fnames = os.listdir(self.__jmx_dir)

        for jmeter_fname in jmeter_fnames:
            # dir
            report = self.__report_dir + \
                     jmeter_fname.split(".")[0] + "{}max_queue".format(self.max_queue)
            # logdir
            log = self.__log_dir \
                  + jmeter_fname.split(".")[0] + "{}max_queue".format(self.max_queue) + ".jtl"
            # report出力用のdirを作成
            self.__output_txt += "\tmkdir " + report + "\n"
            self.__output_txt += "\ttime timeout {} ./jmeter -n -t {} -l {} -e -o {}\n". \
                format(self.time_limit, os.path.join(HOME_DIR, "jmx_files/ml_eco",jmeter_fname), log, report)
            # self.__output_txt+="\techo {}_`date \"+%Y/%m/%d/%H:%M\"`>>jmeter.log\n".format(report)

            self.__output_txt += "\tsleep {}\n".format(self.__sleep_time)











        # def write_connection_line(self):
        #   '''
        #  user数以上のconnectionをスペース区切りで出力する
        # :return:
        # '''
        # output_txt=""
        # for con in CONNECTIONS:
        #    if con>=self.__num_of_users:
        #       output_txt+=str(con)+" "


        # return output_txt


if __name__ == "__main__":
    writer = ShellWriter()
    #    def exe(self, jmx_dir, report_dir, log_dir, output_fname):

    report_dir = "~/IDEetc/apache-jmeter-3.2/bin/reports/report_receiver/"
    log_dir = "~/IDEetc/apache-jmeter-3.2/bin/logs/log_receiver/"

    # writer.exe("/home/shibaken/IDEetc/apache-jmeter-3.2/bin/jmx_files/1_16users/","/home/shibaken/IDEetc/apache-jmeter-3.2/bin/report_dir/",
    #         "/home/shibaken/IDEetc/apache-jmeter-3.2/bin/log_dir/","test.sh",120,"w")
    #         [1,8,16,32,64,128]
    writer.exe("/home/shibaken/PycharmProjects/load_testing_mlflow/ml_eco/", report_dir, log_dir, "./test.sh", 97200,
               3600, 1000, "w")
    # for num in [8,16,32,64,128]:
    #    for rps in ["1_50","50_100","100_200"]:
    #       writer.exe("/home/shibaken/IDEetc/apache-jmeter-3.2/bin/jmx_files/hello_world_sleep/{}RPS/{}users/".format(rps,num),
    #         "/home/shibaken/IDEetc/apache-jmeter-3.2/bin/reports/report_process/",
    #        "/home/shibaken/IDEetc/apache-jmeter-3.2/bin/logs/log_process/", "test.sh",num,480,60,"a")
