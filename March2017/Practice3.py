'''
20170308
高橋：「数値計算」（岩波）3章の実装。　
台形則による積分近似
'''
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s=%(levelname)s=%(message)s')


class integral():
    def trapezoid(self,a,b,f,limit):
        '''
        台計則による近似。分割点を2倍ずつ増やしていく
        :param a:積分の始点
        :param b: 積分終点
        :param f:　1変数の被積分関数
        :param limit: 分割の回数
        :return:
        '''
        #終点条件
        eps=10**-2
        N=1
        h=b-a
        #初期値
        T=h*(f(a)+f(b))/2

        for i in range(limit):
            N=2*N
            h=h/2
            s=0
            for i in range(1,N,2):
                s=s+f(a+i*h)

            newT=T/2+h*s

            if abs(newT-T)<eps*abs(newT):

                return newT
            T=newT

        logging.warning("limitの回数では収束しませんでした")
        return newT

if __name__ == '__main__':
    test=integral
    def f(x):
        return x**3


    #d(self, a, b, f, limit)
    print(test.trapezoid(f,-1,1,f,3))

