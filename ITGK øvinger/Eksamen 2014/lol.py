def myst(A):
    L=len(A) 
    if(L>1):
        B=A[0]*A[L-1]
        return B+myst(A[1:L-1])
    return 0
print(myst([1,2,3,3,2,1]))