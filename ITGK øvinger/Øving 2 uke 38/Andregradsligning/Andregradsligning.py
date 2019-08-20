from math import*
print('Fyll inn tall til ligningen ax^2+bx+c=0')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d=b**2-4*a*c
if d<0:
    print(f'Andregradsligningen {a}*x^2 + {b}*x + {c} har to imaginære løsninger')
elif d>0:
    løs1 = (-b+sqrt(d))/(2*a)
    løs2 = (-b-sqrt(d))/(2*a)
    print(f'Andregradsligningen {a}*x^2 + {b}*x + {c} har to reelle løsninger {løs1} og {løs2}')
elif d==0:
    løs= (-b+sqrt(d))/(2*a)
    print(f'Andregradsligningen {a}*x^2 + {b}*x + {c} har en reell dobbeltrot {løs}')