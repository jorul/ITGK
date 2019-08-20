def myst(A):
    L=len(A)-1
    for i in range(len(A)//2):
        t=A[i]
        A[i] = A[L-i]
        A[L-i]=t
    return A

print(myst([1,2,3,5,7,9]))

import random
def myst3(a):
    b =[0]*len(a)
    for c in range(len(a)):
        d = random.randint(0,len(a)-1)
        b[c] = a[d]
        del a[d]    #del fjerner et bestemt element i listen, her fjerner det a[d].
    return b
print(myst3([1,2,3,4,5,6,7,8,9,10]))

liste = [4, 9, 6, 3, 8, 7, 5]
print(liste[-2:6])

navn = ['Carina', 'erik', 'Magnus', 'Miriam']
navn[1] = 'Erik'
print(navn)

liste1 = [1,3,2,5,4,6]
liste1.sort()
liste2 = [7, 8, 9]
liste3 = liste1+liste2
liste3.insert(9, 10)
liste3.remove(1)
liste3.reverse()
print(liste3)