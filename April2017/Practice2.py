''''
線形回帰モデルのパラメータ推定、t値,F値を
出力するプログラム'''
import numpy as np

class LinearRegression:
    def __init__(self,y,X):
        self.alpha=None
        self.X=X
        self.y=y
        self.fit(y,x)
        self.resid=self.calc_resid()
        self.sig2=self.calc_sig2()



    def fit(self,y,X):
        '''
        線形回帰モデルのパラメータOLSで推定し返す
        :param y:
        :param X:
        :return:
        '''
        xx_inv= np.linalg.inv(np.dot(X.T, X))
        Xy = np.dot(X.T, y)
        self.beta=np.dot(xx_inv,y)



    def calc_resid(self):
        '''
        残差を計算する
        :return:
        '''
        self.y_pred=np.dot(self.X,self.beta)
        return self.y-self.y_pred


    def calc_sig2(self):
        '''
        回帰標準誤差を返す
        :return:
        '''
        return np.dot(self.resid,self.resid)/(self.X.shape[0]-self.X.shape[1])


    def calc_var(self):
        '''
        回帰係数の分散推定値
        :return:
        '''

        self.var= self.sig2* np.linalg.inv(np.dot(self.X.T, self.X))


