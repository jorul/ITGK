def payment(billettpris, antall_biletter):
    if antall_biletter <= 3:
        return antall_biletter*billettpris
    elif antall_biletter>3:
        return antall_biletter*billettpris*0.9

def get_price(konsertnavn):
    f = open('prices.txt','r')
    liste_fra_fil =[]
    for linje in f:
        linje_liste = (linje.strip()).split(';')
        liste_fra_fil.append(linje_liste)
    f.close()
    for i in range(len(liste_fra_fil)):
        if liste_fra_fil[i][0] ==konsertnavn:
            return int(liste_fra_fil[i][1])
    return -1

def til_høyre(venstre,høyre):
    print(venstre.rjust(20), end = '')
    print(høyre.rjust(21))



def ticket(navn, konsertnavn, antall_biletter):
    pris_pr_bilett = get_price(konsertnavn)
    pris_totalt =payment(pris_pr_bilett,antall_biletter)

    for i in range(41):
        print('*', end = '')
    print('Uka 2015')
    for i in range(41):
        print('*', end = '')
    til_høyre('Navn:', navn)
    til_høyre('Konsert:', konsertnavn)
    til_høyre('Antall billetter:', str(antall_biletter))
    pris = str(pris_totalt) + ' kr'
    til_høyre('Totalpris', pris)
    
def write_to_file(navn, konsertnavn, antall_biletter,filnavn):
    pris_pr_bilett = get_price(konsertnavn)
    pris_totalt = payment(pris_pr_bilett,antall_biletter)
    linje = f'{konsertnavn};{str(antall_biletter)};{str(pris_totalt)};{navn} \n'
    f = open(filnavn,'a')
    f.write(linje)
    f.close

def biletter_konsert(liste_fra_fil):
    konsertnavn = input('Hvilken konsert ønsker du bilettsalget til? ')
    bilettsalg = 0
    for i in range(len(liste_fra_fil)):
        if liste_fra_fil[i][0] == konsertnavn:
            bilettsalg += liste_fra_fil[i][1]
    print(f'Til konserten med {konsertnavn} er det totalt solgt {bilettsalg} biletter')


def inntekt_konsert(liste_fra_fil):
    konsertnavn = input('Hvilken konsert ønsker du inntekten til? ')
    inntekt = 0
    for i in range(len(liste_fra_fil)):
        if liste_fra_fil[i][0] == konsertnavn:
            inntekt += liste_fra_fil[i][2]
    print(f'Konserten med {konsertnavn} har totalt innbrakt {inntekt} kr')

def inntekt_totalt(liste_fra_fil):
    inntekt = 0
    for i in range(len(liste_fra_fil)):
        inntekt += liste_fra_fil[i][2]
    print(f'Totalt har arrangementet hatt en inntekt på {inntekt} kr')


def main():
    f = open('concerts.txt','r')
    liste_fra_fil =[]
    for linje in f:
        linje_liste = (linje.strip()).split(';')
        liste_fra_fil.append(linje_liste)
    f.close()

    print('********** MENY UKA 2015 **********')
    print('0 = avslutt')
    print('1 = antall biletter solgt til en konsert')
    print('2 = inntekt en konsert')
    print('3 = inntekt totalt')
    valg = int(input('Hva vil du gjøre? '))
    while valg != 0:
        if valg == 1:
            biletter_konsert(liste_fra_fil)
        elif valg == 2:
            inntekt_konsert(liste_fra_fil)
        elif valg == 3:
            inntekt_totalt(liste_fra_fil)
        else:
            print('Ikke gyldig input')

        print('0 = avslutt')
        print('1 = antall biletter solgt til en konsert')
        print('2 = inntekt en konsert')
        print('3 = inntekt totalt')
        valg = int(input('Hva vil du gjøre? '))
    


