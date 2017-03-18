'''
巡回セールスマン問題
'''
from math import sqrt,exp
from numpy import empty
from random import random,randrange



N=25
R=0.02

Tmax=x=10.0
Tmin=1e-3
tau=1e4


#原点からの距離
def norm(x):
    return sqrt(x[0]**2+x[1]**2)



#距離
def distance(r,N):
    '''

    :param N:都市の数
    :param r: 都市の位置ベクトル
    :return:
    '''
    s=0.0
    for i in range(N):
        s+=norm(r[i+1]-r[i])
        return s


r=empty([N+1,2],float)
for i in range(N):
    r[i,0]=random()
    r[i,1]=random()
r[N]=r[0]
D=distance(r,N)

t=0
T=Tmax

while T>Tmin:
    t+=1
    T=Tmax*exp(-t/tau)

    i,j=randrange(1,N),randrange(1,N)
    while i==j:
        i, j = randrange(1, N), randrange(1, N)
    oldD=D
    r[i,0],r[j,0]=r[j,0],r[i,0]
    r[i,1],r[j,1]=r[j,1],r[i,1]
    D=distance(r,N)
    delta=D-oldD
    if random()>exp(-delta/T):
        r[i,0],r[j,0]=r[j,0],r[i,0]
        r[i,1],r[j,1]=r[j,1],r[i,1]
        D=oldD

    print(D)
