#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bs4
import  requests

#error_rateを読み取る
####################################################################
target_fname="/home/shibaken/IDEetc/apache-jmeter-3.2/bin/report_dir/process2_connection16_32users_50_100RPS_s2/content/js/dashboard.js"




def  get_error_rate(fname):
    '''
    jmeterをshellで実行した時のerror_rateを抽出する関数
    :param fname:
    :return:
    '''
    with open(target_fname, "r")as reader:
        tmp = ""
        x = False
        for line in reader:
            if line.__contains__("createTable($(\"#statisticsTable\")"):
                tmp += line
                break

    return tmp.split(",")[5].strip()
