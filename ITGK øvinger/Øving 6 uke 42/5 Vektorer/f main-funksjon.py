import random
def make_vec():
    listami = []
    for i in range (3):
        listami.append(random.randint(-10,11))
    return listami


def vector_print(vektor, navn):
    print(f'{navn} = {vektor}')

def skalarmultiplikasjon(liste, skalar):
    nyliste = []
    for i in range (len(liste)):
        nyliste.append(' ')
    for i in range (len(liste)):
        nyliste [i] = liste [i]*skalar
    return nyliste

import math
def vec_len(vektor):
    summen = 0
    for i in range (len(vektor)):
        summen += (vektor [i])**2
    return math.sqrt(summen)

def vector_dot_product(vektor1,vektor2):
    if len(vektor1) != len(vektor2):
        print ('Vektorene du ga meg har ikke samme lengde, da er min oppgave umulig, din fjompenisse.')
    summen = 0
    for i in range (len(vektor1)):
        summen += vektor1 [i] * vektor2[i]
    return summen


def main():
    vec1 = make_vec()
    vector_print(vec1, 'vec1')
    skalar = int(input('Skriv inn en skalar: '))
    
    lengdefør = vec_len(vec1)
    lengdeetter = vec_len(skalarmultiplikasjon(vec1, skalar))
    print(f'lengden før skalering var: {lengdefør}')
    print(f'Lengden etter skalering er: {lengdeetter}')
    print(f'Forholdet mellom lengden før og etter skalering er: {lengdeetter/lengdefør}')
    vec3 = make_vec()
    print("Prikkproduktet av",vec1,"og",vec3,"er:",format(vector_dot_product(vec1,vec3),".3f"))
main()