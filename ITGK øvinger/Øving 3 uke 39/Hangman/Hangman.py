hemmelig_ord = str.lower(input('Skriv inn det hemmelige ordet: '))
antall_liv = int(input('Hvor mange forsøk får brukeren?  '))
hemmelig_liste = list(hemmelig_ord) # lager en liste som består av bokstavene i det hemmelige ordet
brukte_bokstaver = [] # lager en liste som fylles med bokstavene som er brukt


sjekk_liste = list(hemmelig_ord) 
for i in range(len(sjekk_liste)):
    sjekk_liste[i] = '_' # listen blir til bare understreker, men vil endres når brukeren gjetter riktig

for i in range(25):
    print('\n')


print(f'Okei, du har {antall_liv} liv. La oss spille hangman!')
while sjekk_liste != hemmelig_liste:
    print(' '.join(sjekk_liste))
    if brukte_bokstaver != []:
        print('Brukte bokstaver:', ' '.join(brukte_bokstaver))
    bokstav = str.lower(input('Gjett én bokstav i ordet: '))
   
    if bokstav in hemmelig_liste:
        for i in range(len(sjekk_liste)):
            if hemmelig_liste[i] == bokstav:
                sjekk_liste [i] = bokstav
        print('\n \n \n \n \n \n')
    else:
        print('\n \n \n \n \n \n')
        print(f'Bokstaven {bokstav} er ikke i ordet')
        antall_liv = antall_liv-1
        if antall_liv == 0:
            print(f'Du har ingen liv igjen. Ordet var {hemmelig_ord}')
            break
        brukte_bokstaver.append (bokstav)
    print(f'Du har {antall_liv} liv igjen.') 
if sjekk_liste == hemmelig_liste:
    print(f'Korrekt! ordet var {hemmelig_ord}.')