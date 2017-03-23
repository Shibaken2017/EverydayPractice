'''
・2つの状態遷移をランダムに選ぶ
・その軌跡をplotする
'''
import matplotlib.pyplot as plt
import random

def transformation_1(p):
    x=p[0]
    y=p[1]
    return x+1,y-1

def transformation_2(p):
    x=p[0]
    y=p[1]
    return x+1,y+1


def transform(p):
    transformations=[transformation_1,transformation_2]
    t=random.choice(transformations)
    x,y=t(p)
    return x,y

def build_trajectory(p,n):
    x=[p[0]]
    y=[p[1]]

    for i in range(n):
        p=transform(p)
        x.append(p[0])
        y.append(p[1])

    return x,y


if __name__=="__main__":
    #始点
    p=(1,1)
    n=100
    x,y=build_trajectory(p,n)
    plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()