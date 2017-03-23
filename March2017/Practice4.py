'''
(1)各ユーザーのプロフィールを予測した結果ファイル,2)各ユーザーのプロフィールの正解ファイル
をまとめ、出力するクラス
'''

import os
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s=%(levelname)s=%(message)s')


class user:
    '''
    各ユーザ
    (1)screenName(2)予測結果(3)成果解データを保持する
    '''

    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.predict = ""
        self.answer = ""

    def is_ok(self):
        '''
        予測が正しければ1を返す
        :return:
        '''
        if self.predict == self.answer:
            return 1
        else:
            return 0

    def write_txt(self):
        return self.screen_name + "\t" + self.answer + "\t" + self.predict + "\n"


class checker():
    def __init__(self):
        self.user_dict = {}

    def load(self, predict_fname, answer_fname):
        self.user_dict = {}
        self.predict_num={}

        # 書式はscreen_name\t予測プロフィール\n
        with open(predict_fname, "r", encoding="UTF-8")as reader:
            for line in reader:
                tmp = line.split("\t")
                tmp_screen_name = tmp[0]
                tmp_user = user(tmp_screen_name)
                tmp_predict = tmp[1].replace("\n", "")
                tmp_user.predict = tmp_predict
                # 初期値としてunknown
                tmp_user.answer = "unknown"
                self.user_dict[tmp_screen_name] = tmp_user
        # 書式はscreen_name\t予測プロフィール\n
        with open(answer_fname, "r", encoding="UTF-8")as reader:
            for line in reader:
                tmp = line.split("\t")
                tmp_screen_name = tmp[0]
                # predictファイルに無いユーザーについては無視
                if tmp_screen_name in self.user_dict.keys():
                    self.user_dict[tmp_screen_name].answer = tmp[1].replace("\n", "")
        #答え合わせ
        self.is_ok()


    def is_ok(self):
        '''
        全ユーザーについて答え合わせ
        :return:
        '''
        for user in self.user_dict.values():
            user.is_ok()

    def straified_answer(self):

        '''
        層別化した答えを返す
        '''
        predict_num_dict = {}
        actual_num_dict = {}
        for user in self.user_dict.values():
            predict_num_dict.setdefault(user.predict, 0)
            predict_num_dict[user.predict] += 1
            actual_num_dict.setdefault(user.predict, 0)
            if user.is_ok() == 1:
                actual_num_dict[user.predict] += 1
        output_txt="層別化正答率\n"
        for prof in actual_num_dict.keys():
            output_txt+=prof+"\t"+str(predict_num_dict[prof])+"\t"+str(actual_num_dict[prof])+"\n"
        return output_txt
    def write_txt(self, output_fname):

        '''
        ユーザー名、正解、予測、をタブ区切りで出力
        :param output_fname:
        :return:
        '''
        with open(output_fname, "w", encoding="UTF-8")as writer:
            #層別化正答数
            writer.write(self.straified_answer())
            writer.write("\n詳細\n")
            writer.write("screen_name" + "\t" + "answer" + "\t" + "predict\n")
            for user in self.user_dict.values():
                writer.write(user.write_txt())


if __name__ == '__main__':
    test = checker()
    test.load("testdata/predict.txt", "testdata/answer.txt")
    test.is_ok()
    test.write_txt("testdata/example.txt")
