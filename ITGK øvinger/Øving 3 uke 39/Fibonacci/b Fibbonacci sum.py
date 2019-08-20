antall = int(input('Hvilket fibbonaccitall ønsker du? '))

def fib(x):
    if x==0 or x==1:
        return x
    else:
        return fib(x-1) + fib(x-2)
b=0
for i in range (antall+1):
    a = fib(i)
    b = b+a
print(f'Fibonaccitall nummer {antall} er {a}')
print(f'Summen av de {antall} første fibonaccitallene er {b}')