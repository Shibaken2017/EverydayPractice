'''
自然数1～Nの中で素数が占める割合を求める関数
'''
from sympy import FiniteSet,pi
def probability(space,event):
    return len(event)/len(space)


def check_prime(number):
    if number !=1:
        for factor in range(2,number):
            if number%factor==0:
                return False
    else:
        return False
    return True


if __name__=='__main__':

    space=FiniteSet(*range(1,21))
    print(space)
    primes=[]
    for num in space:
        if check_prime(num):
            primes.append(num)

    event=FiniteSet(*primes)
    p=probability(space,event)


    print("標本空間{}".format(space))
    print("素数{}".format(event))
    print("素数の確率確率{}".format(p))