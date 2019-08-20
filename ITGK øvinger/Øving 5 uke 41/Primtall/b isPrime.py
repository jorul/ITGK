def divisable(a,b):
    return a%b == 0

def isPrime(x):
    for b in range(2,x-1):
        if divisable(x,b) == True:
            return False
            break
    return True
        



print(isPrime(11))           #printer True
print(isPrime(15))           #printer False