''''
線形回帰モデルのパラメータ推定、t値,F値を
出力するプログラム'''
import numpy as np

class LinearRegression:
    def __init__(self,y,X):
        self.X=X
        self.y=y
        self.beta=self.fit(y,X)
        self.resid=self.calc_resid()
        self.sig2=self.calc_sig2()



    def fit(self,y,X):
        '''
        線形回帰モデルのパラメータOLSで推定し返す
        :param y:
        :param X:
        :return:
        '''
        XX = np.linalg.inv(np.dot(X.T, X))
        Xy = np.dot(X.T, y)
        return np.dot(XX,y)

    def calc_resid(self):
        '''
        残差を計算する
        :return:
        '''
        y_pred=np.dot(self.X,self.beta)
        return self.y-y_pred


    def calc_sig2(self):
        '''
        回帰標準誤差を返す
        :return:
        '''
        return np.dot(self.resid,self.resid)/(self.X.shape[0]-self.X.shape[1])
import numpy as np
X=np.array([[1,2],[3,4]])
y=np.array([[1],[2]])

np.dot(X,y)
XX=  np.linalg.inv(np.dot(X.T,X))
Xy=np.dot(X.T,y)
