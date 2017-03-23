def find_min(L,b):
    '''
    配列Lのb以降の要素で最も小さい要素のindexを返す。
    ＞＞find_min([3,-1,7,5],2)
    3

    :param L:
    :param b:
    :return:
    '''
    smallest=b
    i=b+1
    while i!=len(L):
        if L[i]<L[smallest]:
            smallest=i

        i=i+1

    return smallest



def selection_sort(L):
    '''
    配列Lを昇順にsortする
    :param L:
    :return:
    '''
    i=0
    while i!=len(L):
        smallest=find_min(L,i)
        L[i],L[smallest]=L[smallest],L[i]
        i+=1
    return L


if __name__=='__main__':
    print(selection_sort([3,2,1]))
