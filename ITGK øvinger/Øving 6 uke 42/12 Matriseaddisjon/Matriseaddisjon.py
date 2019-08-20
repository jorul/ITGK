import random
def random_matrise(bredde, høyde):
    indre_matrise = []
    ytre_matrise = []
    for h in range(høyde):
        for b in range(bredde):
            indre_matrise.append(random.randint(0,11))
        ytre_matrise.append(indre_matrise)
        indre_matrise = []
    return ytre_matrise

def print_matrise(matrise, navn):
    print(f'{navn}= [')
    for i in range(len(matrise)):
        print(matrise[i])
    print(']')

def matrise_addisjon(a,b):
    ytre_addisjonsmatrise = []
    indre_addisjonsmatrise = []
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print('Matrisene er ikke av samme dimensjon')
    else:
        for h in range (len(a)):
            for s in range (len(a[0])):
                tall = a[h][s] + b[h][s]
                indre_addisjonsmatrise.append(tall)
            ytre_addisjonsmatrise.append(indre_addisjonsmatrise)
            indre_addisjonsmatrise = []
    return ytre_addisjonsmatrise

def main():
    A = random_matrise(4,3)
    print_matrise(A, 'A')
    B = random_matrise(3,4)
    print_matrise(B, 'B')
    C = random_matrise(3,4)
    print_matrise(C, 'C')
    D = matrise_addisjon(A,B)
    E = matrise_addisjon(B,C)
    print_matrise(E, 'B+C' )

main()