'''
2017_03_10
linear sarch,の実装方法の違いによる速度比較の練習
'''
import time

def linear_search1(input_list,value):
    '''
    input_listにvalueがあればそのindexを返す。なければ-1が返される
    :param input_list:
    :param value:
    :return:
    '''
    i=0
    while i!=len(input_list) and input_list[i]!=value:
       i+=1

    if i==len(input_list):
        return -1
    else:
        return i
def linear_search2(input_list,value):
    for i in range(len(input_list)):
        if input_list[i]==value:
            return i



    return -1
def linear_search3(input_list,value):
    input_list.append(value)
    i=0

    while input_list[i]!=value:
        i+=1
    input_list.pop()

    if i==len(input_list):
        return -1
    else:
         return i

def time_it(search,L,v):
    t1=time.perf_counter()
    search(L,v)
    t2=time.perf_counter()
    return (t2-t1)*1000.0

def print_times(v,L):
    #標準搭載関数での処理時間
    t1=time.perf_counter()
    L.index(v)
    t2=time.perf_counter()
    index_time=(t2-t1)*1000.0

    while_time=time_it(linear_search1,L,v)
    for_time=time_it(linear_search2,L,v)
    sentinel_time=time_it(linear_search3,L,v)

    print("index関数:{}\t while:{}\tfor:{}\nsentinel:{}\t".format(index_time,while_time,for_time,sentinel_time))



if __name__ == '__main__':
    L=list(range(1000001))
    print_times(10,L)
    print_times(5000,L)
    print_times(10000,L)