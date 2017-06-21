#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

SSH = "aiueo"


class ShellWriter:
    '''
    複数のjmxファイルを実行するためのシェルスクリぷとを書き出すこ＾ーど０
    各テストごとにsleep時間を入れる

    '''

    def __init__(self):
        print "nyan"

    def exe(self, jmx_dir, report_dir, log_dir, output_fname):
        '''
          :param jmx_dir:
          :param report_dir:
          :param log_dir:
          :return:
          '''
        self.__output_txt = ""
        self.__jmx_dir = jmx_dir
        self.__log_dir = log_dir
        self.__report_dir = report_dir
        self.write_initial_part()
        self.write_jmeter_part()
        with open(output_fname, "w")as writer:
            writer.write(self.__output_txt)


    def write_initial_part(self):
        self.__output_txt += "for process in 1\n"
        self.__output_txt += "for connection in 8\n"
        self.__output_txt += "do\n"


    def write_jmeter_part(self):
        # jmeter -n -t my_test.jmx -l log.jtl -e -o report
        jmeter_fnames = os.listdir(self.__jmx_dir)

        for jmeter_fname in jmeter_fnames:
            report = self.__report_dir + "process${process}_connection${connection}_" \
                     + jmeter_fname.split(".")[0]

            log = self.__log_dir + "process${process}_connection${connection}_" \
                  + jmeter_fname.split(".")[0] + ".jtl"

            # base="process{}_connection{}_".format(process,connection)+fname.split(".")[0]

            self.__output_txt += "\tjmeter -n -t {} -l {} -e -o {}\n".format(self.__jmx_dir + jmeter_fname, log, report)

        self.__output_txt += "done\n"


if __name__ == "__main__":
    writer = ShellWriter()
    #    def exe(self, jmx_dir, report_dir, log_dir, output_fname):

    writer.exe("./jmx_files/","./report_dir/","./log_dir/","test.sh")
