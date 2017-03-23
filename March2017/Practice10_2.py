'''
さいころをmax_rolls回投げた時にtarget_score以上の合計値を出せる確率求める関数
'''

from sympy import FiniteSet
import random
def find_prob(target_score,max_rolls):
    die_sides=FiniteSet(1,2,3,4,5,6)
    #標本空間
    s=die_sides**max_rolls
    if max_rolls>1:
        success_rolls=[]
        for elem in s:
            if sum(elem)>=target_score:
                success_rolls.append(elem)
    else:
        if target_score>6:
            success_rolls=[ ]
        else:
            success_rolls=[]
            for roll in die_sides:
                if roll >=target_score:
                    success_rolls.append(roll)

    e=FiniteSet(*success_rolls)

    return len(e)/len(s)

if __name__=='__main__':
    target_score=25
    max_rolls=5
    p=find_prob(target_score,max_rolls)
    print("probability:{}".format(p))
