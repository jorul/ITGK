antall = int(input('Hvor mange fibbonaccitall ønsker du? '))
def fib(x):
    if x==0 or x==1:
        return x
    else:
        return fib(x-1) + fib(x-2)
listen = []
b = 0
print(f'Her er de {antall} første fibbonaccitallene:')
for i in range (1, antall+1):
    a = fib(i)
    listen.append(a)
    b= b+a
print(listen)
print(b)