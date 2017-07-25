#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bs4
import  requests
import csv
import os
#error_rateを読み取る
####################################################################
#target_fname="/home/shibaken/IDEetc/apache-jmeter-3.2/bin/report_dir5/process2_connection128_64users_1_50RPS_s3/content/js/dashboard.js"

def  get_error_rate(fname):
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

    return tmp.split(",")[6].strip()


#target_fname="/home/shibaken/IDEetc/apache-jmeter-3.2/bin/report_dir5/process2_connection128_64users_1_50RPS_s3/content/js/dashboard.js"
target_fname="/home/shibaken/IDEetc/apache-jmeter-3.2/bin" \
             "/report_dir5/process3_connection64_8users_1_50RPS_s3/content/js/dashboard.js"

#print get_error_rate(target_fname)








def make_csv(fname_form,connection,process,target_dir,output_dir,users_list,rps_list):

    if not os.path.exists(target_dir):
        raise Exception("dirがありませｎ")
    csv_fname=os.path.join(output_dir,"process{}connection{}.csv".format(process,connection))

    with open(csv_fname,"w")as writer:
        output_writer = csv.writer(writer)
        initial_line=[""]
        initial_line.extend(rps_list)
        output_writer.writerow(initial_line)
        for user in users_list:
            each_line=[str(user)+"users"]
            for rps in rps_list:

                # process2_connection128_64users_1_50RPS_s3
                #fname_form = "process{}_connection{}_{}users_{}_s3"
                dir_name=os.path.join(target_dir,fname_form.format(process,connection,user,rps))
                fname=os.path.join(dir_name,"content/js/dashboard.js")
                #print fname
                if os.path.exists(fname):
                    print "okokoko"
                    print fname
                    print get_error_rate(fname)
                    #小数点以下切り捨てround(val,2)
                    each_line.append(round(float(get_error_rate(fname)),1))
                else:
                    each_line.append("None")
            output_writer.writerow(each_line)

#def make_csv(fname_form,connection,process,target_dir,output_dir,users_list,rps_list):
fname_form="process{}_connection{}_{}users_{}_s3"


if __name__=="__main__":
    connection_list=[8,16,32,64,128,256]
    process_list=[1,2,3]

    for con in connection_list:
        for pro in process_list:

            #already/report_dir/
            make_csv(fname_form,con,pro,"/home/shibaken/IDEetc/apache-jmeter-3.2/bin/already/report_dir/",
                 "./hello_world/s3_average_response_time/",[1,8,16,32,64,128],["1_50RPS","50_100RPS","100_200RPS"])


    #process2_connection128_64users_1_50RPS_s3
    #fname_form="process{}_connection{}_{}users_{}_s3"

