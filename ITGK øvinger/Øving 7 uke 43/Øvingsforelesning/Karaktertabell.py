karakterer = [['' for x in range (7)] for y in range(6)]

karakterer[0] = ['',1,2,3,4,'Tot','Kar']
for i in range(1,6):
    karakterer[i][0] = input('Oppgi navn: ')

import random
def fyll_tabell(karTabell):
    for i in range(1,6):
        for j in range(1,5):
            karTabell[i][j] = random.randint(50,100)
    return karTabell
karakterer = fyll_tabell(karakterer)

import math
def beregn_snitt(karTabell):
    for i in range(1,6):
        summ = 0
        for j in range (1,5):
            summ += karTabell[i][j]
        karTabell[i][j+1] = math.ceil(summ/(len(karTabell[i])-3))
    return karTabell

karakterer = beregn_snitt(karakterer)

def extra_pretty(kar):
    for i in range (len(kar)):
        for j in range(len(kar[0])):
            print(kar[i][j], end='\t')
        print()

extra_pretty(karakterer)
