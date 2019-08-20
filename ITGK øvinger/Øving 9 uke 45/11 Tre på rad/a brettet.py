def brett(brettet):
    print('    1   2   3')
    print('  -------------')
    print(f'1 | {brettet[0][0]} | {brettet[0][1]} | {brettet[0][2]} |')
    print('  -------------')
    print(f'2 | {brettet[1][0]} | {brettet[1][1]} | {brettet[1][2]} |')
    print('  -------------')
    print(f'3 | {brettet[2][0]} | {brettet[2][1]} | {brettet[2][2]} |')
    print('  -------------')

def sjekk_vinner(brettet):
    if brettet[0][0]!= ' ' and (brettet[0][0] == brettet[0][1] == brettet[0][2] or brettet[0][0] == brettet[1][0] == brettet[2][0]):
        return brettet[0][0]
    elif brettet[2][2] != ' ' and (brettet[0][2] == brettet[1][2] == brettet[2][2] or brettet[2][0] == brettet[2][1] == brettet[2][2]):
        return brettet[2][2]
    elif brettet[1][1] != ' ' and(brettet[1][0] == brettet[1][1] == brettet[1][2] or brettet[0][2] == brettet[1][1] == brettet[2][0] or brettet[0][0] == brettet[1][1] == brettet[2][2] or brettet[0][1] == brettet[1][1] == brettet[2][1]):
        return brettet[1][1]
    else:
        return False

def sjekk_lov(rad,kolonne,brettet):
    try:
        rad -=1
        kolonne -= 1
        if brettet[rad][kolonne] == ' ':
            return True
        else:
            return False
    except:
        return False

def riktig(rad, kolonne):
    if (rad == 1 or rad == 2 or rad == 3) and (kolonne == 1 or kolonne == 2 or kolonne == 3):
        return True
    else:
        return False

import random

def tre_paa_rad():
    print('Da skal vi spille tre på rad!')
    person_x = input("Hvem vil spille som 'x'? ")
    person_o = input("Hvem vil spille som 'o'? ")
    tur = random.choice([person_x, person_o]) #Velger hvem som begynner
    print(f'Den er grei {person_x} og {person_o}, da spiller vi tre på rad!')

    brettet = [[' ', ' ', ' '], [' ', ' ',' '], [' ', ' ', ' ']]

    while sjekk_vinner(brettet) == False:
        brett(brettet) #printer ut brettet
        print(f'Det er {tur} sin tur. Hvor vil du sette en brikke?')
        rad = ''
        kolonne = ''
        spill = True
        while spill == True:
            rad = int(input('rad: '))
            kolonne = int(input('kolonne: '))
            if riktig(rad,kolonne) == False:
                print(f'Det der er ikke en plass på brettet {tur}, plis skjerp deg. Prøv på nytt.')
            elif sjekk_lov(rad,kolonne,brettet) == False:
                print(f'Den plassen er tatt {tur}, plis skjerp deg. Prøv på nytt.')
            else:
                spill = False
        if tur == person_o:
            brettet[rad-1][kolonne-1] = 'o'
            tur = person_x
        else:
            brettet[rad-1][kolonne-1] = 'x'
            tur = person_o
    brett(brettet)
    vinner = sjekk_vinner(brettet)
    if vinner == 'x':
        print(f'Gratulerer {person_x}, du vant!')
        print(f'Bedre lykke neste gang {person_o}.')
    else:
        print(f'Gratulerer {person_o}, du vant!')
        print(f'Bedre lykke neste gang {person_x}.')


tre_paa_rad()