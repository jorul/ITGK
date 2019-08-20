r = float(input('r = '))
n = int(input('n = '))
tol = float(input('toleransegrense = '))
riktig = 1/(1-r)
svar = 0
i = 0
summen = 0
while riktig - svar >= tol:
    svar = (1-r**(i+1))/(1-r)
    i += 1
for x in range(0,n+1):
    summen += r**x
print(f'Summen av rekken er {summen}')
print(f'For å være innenfor toleransegrensen {tol}, kjørte løkken {i} ganger')
print(f'Differansen mellom virkelig verdi og estimert verdi var da {abs(riktig-svar)}')

#Når den egentlige summen - min sum er mindre enn toleransen så kjører while-løkka