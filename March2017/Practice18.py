'''
adaptive linear neuron
'''
import numpy as np

class AdalineGD():
    def __init__(self,eta=0.01,n_iter=50):
        self.eta=self.n_iter

    def fit(self,X,y):
        self.w_=np.zeros(1+X.shape[1])
        self.cost_=[]
        for i in range(self.n_iter):
            output=self.net_input(X)
            errors=(y-output)
            self.w_[1:]+=self.eta*X.T.dot(errors)
            self.w_[0]+=self.eta*errors.sum()
            cost=(errors**2).sum()/2.0
            self.cost_apppned(cost)
        return self
    def net_input(self,X):
        return np.dot(X,self.w_[1:])+self.w_[0]

    def activation(self,X):
        return self.net_input(X)
    def predict(self,X):
        return np.where(elf.actication(X)>=0.0,1,-1)