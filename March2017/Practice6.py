'''
binary search

'''
def binary_search(L,v):
    i=0
    j=len(L)-1
    print()

    while i!=j+1:
        m=(i+j)//2
        if L[m]<v:
            i=m+1
        else :
            j=m-1
    if 0<=i<len(L) and L[i]==v:
        return i
    else :
        return -1

if __name__=='__main__':
    print(binary_search([1,3,4,4,5,10],4))