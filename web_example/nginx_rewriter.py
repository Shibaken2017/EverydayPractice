#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys


class NginxReWriter:
    '''
    指定したngnxのprocessとconectionを書き換える
    '''

    def __init__(self):
        print "nyan"

    def rewrite(self, conf_fname, process, connection):
        if not os.path.exists(conf_fname):
            raise Exception(conf_fname + "は存在しません")

        output_txt = ""
        with open(conf_fname, "r")as reader:
            # print reader.readlines()
            for line in reader:
                if line.__contains__("worker_processes"):
                    output_txt += "worker_processes {};\n".format(process)

                elif line.__contains__("worker_connections"):
                    output_txt += "worker_connections {}:\n".format(connection)

                else:
                    output_txt += line

        with open(conf_fname, "w")as writer:
            writer.write(output_txt)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 4:
        raise Exception("引数が足りません")

    writer = NginxReWriter()
    writer.rewrite(args[1], args[2], args[3])

    #reload the nginx.conf
    os.system("echo abcdefg >> test.txt")
    os.system("sudo nginx -s reload")
    print "finish"