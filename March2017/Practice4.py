'''
各ユーザーのプロフィールを予測した結果とその正解ファイルがあるとし
結果を一つのファイルにまとめる
'''

import os
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s=%(levelname)s=%(message)s')

class user:
    '''
    各ユーザ
    (1)screenName(2)予測結果(3)成果解データを保持する
    '''
    def __init__(self,screen_name):
        self.screen_name=screen_name
        self.predict=""
        self.answer=""

    def getText(self):
        return self.screen_name+"\t"+self.screen_name+"\t"+self.predict+"\n"

    def isOK(self):
        '''
        予測が正しければ1を返す
        :return:
        '''
        if self.predict==self.answer:
            return 1
        else :
            return 0
    def write_txt(self):
        return self.screen_name+"\t"+self.answer+"\t"+self.predict+"\n"



class checker():
    def __init__(self):
        self.user_dict={}
    def load(self,predict_fname,answer_fname):
        self.user_dict={}
        #書式はscreen_name\t予測プロフィール\n
        with open(predict_fname,"r",encoding="UTF-8")as reader:
            for line in reader:
                tmp = line.split("\t")
                tmp_screen_name = tmp[0]
                tmp_user = user(tmp_screen_name)
                tmp_predict = tmp[1].replace("\n", "")
                tmp_user.predict = tmp_predict
                self.user_dict[tmp_screen_name] = tmp_user
        #書式はscreen_name\t予測プロフィール\n
        with open(answer_fname, "r", encoding="UTF-8")as reader:
            for line in reader:
                tmp = line.split("\t")
                tmp_screen_name = tmp[0]
                #predictファイルに無いユーザーについては無視
                if tmp_screen_name in self.user_dict.keys():
                    self.user_dict[tmp_screen_name].answer = tmp[1].replace("\n", "")


