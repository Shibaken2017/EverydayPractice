#!/usr/bin/env python
# -*- coding: utf-8 -*-

#process数ごとに結果をcsv出力する
#connection,RPSごとにprocess,userの表が作り出される
import os
import csv
ERROR_RATE=5
RESPONSE_TIME=6



def  extract_info(fname,target_indicator):
    '''
    jmeterをshellで実行した時のerror_rateを抽出する関数
    :param fname:
    :return:
    '''

    with open(fname, "r")as reader:
        tmp = ""
        x = False
        for line in reader:
            if line.__contains__("createTable($(\"#statisticsTable\")"):
                tmp += line
                break

    return tmp.split(",")[target_indicator].strip()






def summarize_by_process(output_fname,target,target_dir,fname_form,connection,process_list,users_list):
    #process10_connection128_16users_50_100RPS_s3
    #process{}_connection{}_{}users_50_100RPS_s3
    with open(output_fname,"w")as writer:
        output_writer=csv.writer(writer)
        init_line=[""]
        init_line.extend(users_list)

        output_writer.writerow(init_line)
        fnames_list = os.listdir(target_dir)
        for process in process_list:
            output_line=[process]
            for user in users_list:
                fname=os.path.join(target_dir,fname_form.format(process,connection,user),"content/js/dashboard.js")
                if os.path.exists(fname):
                    num=extract_info(fname,target)
                    output_line.append(num)


                else:
                    print fname
                    output_line.append("None")


            output_writer.writerow(output_line)




if __name__=="__main__":
    #def summarize_by_process(output_fname,target,target_dir,fname_form,connection,process_list,users_list):
    for connection in [256]:
        fname_form="process{}_connection{}_{}users_50_100RPS_s3"
        target_dir="/home/shibaken/IDEetc/apache-jmeter-3.2/bin/reports/report_process/"
    #connection=128
        target=RESPONSE_TIME
        process_list=[i for i in range(1,11)]
        users_list=[32,64,128]
        #output_fname="./test.csv"
        output_fname="connection{}_50_100_RPS_s3.csv".format(connection)

    #def summarize_by_process(output_fname, target, target_dir, fname_form, connection, process_list, users_list):


        summarize_by_process(output_fname,target,target_dir,fname_form,connection,process_list,users_list)