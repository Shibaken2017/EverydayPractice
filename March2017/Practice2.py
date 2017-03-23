'''
2017/3/7
高橋：「数値計算」（岩波）2章の実装。　
1変数関数fのf=0の下位を求めるクラス
'''
class SolveEquation():
    def divide(self,f, a, b, limit):
        '''
              1変数関数fのf=0となる解を二分法により求めるメソッド
          :param f:
          :param a:
          :param b:
          :param limit:
          :return:
          '''

        eps = 0.001

        if f(a) * f(b) > 0:
            raise Exception("f(a)*f(b)>0なので二分法では解が求められません")
        if f(a) > f(b):
            tmp = a
            a = b
            b = tmp

        for i in range(limit):

            c = (a + b) / 2
            if abs(b - a) / 2 < eps:
                return c
            if f(c) > 0:
                b = c
            elif f(c) < 0:
                a = c
            else:
                return c

    def differentiate(self, f, x):
        '''
        1変数関数fのxにおける数値部分値を返すメソッド
        :param f: 微分したい関数
        :param x: 微分したい点
        :return:
        '''
        delta = 0.0001
        return (f(x + delta) - f(x)) / delta

    def newtonMethod(self, f, x, limit):
        '''
        ニュートン法によりf=0となる解を求める
        :param f: 関数
        :param x: 初期値
        :param limit: 反復計算回数
        :return:
        '''
        eps = 0.001
        x_new = 0.0
        diff_f = 0.0
        for i in range(limit):
            diff_f = self.differentiate(f, x)
            if diff_f < eps:
                print("微分が0に収束")
                return x
            x_new = x - f(x) / diff_f

            if abs(x_new - x) < eps * abs(x_new):
                return x_new
            x=x_new
        raise Exception("1000解でも収束しませんでした!")



if __name__ == '__main__':
    test=SolveEquation()
    def f(x):
        return x**3-1
    print(test.divide(f,-3,13,100))
    print(test.newtonMethod(f,100,10000))
