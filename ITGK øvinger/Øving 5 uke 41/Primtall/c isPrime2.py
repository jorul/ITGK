from math import sqrt
def divisable(a,b):
    return a%b == 0

def isPrime2(x):
    if x%2 ==0:
        return False
    upper = round(sqrt(x)+0.5)
    for b in range(3,upper,2):
        if divisable(x,b) == True:
            return False
            break
    return True
        



print(isPrime2(11))           #printer True
print(isPrime2(15))           #printer False