def gcd (a, b):
    while b != 0:
        gammel_b = b
        b = a%b
        a = gammel_b
    return a

a = int(input('a = '))
b = int(input('b = '))
print(gcd(a,b))