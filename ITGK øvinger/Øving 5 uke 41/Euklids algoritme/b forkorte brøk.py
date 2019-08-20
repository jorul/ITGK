def gcd (a, b):
    while b != 0:
        gammel_b = b
        b = a%b
        a = gammel_b
    return a

def reduce_fraction(a,b):
    teller = a//gcd(a,b)
    nevner = b//gcd(a,b)
    return f'{teller}/{nevner}'




a = int(input('a = '))
b = int(input('b = '))
print(reduce_fraction(a,b))