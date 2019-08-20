def sek_paa_benken(ant_paa_laget,ant_paa_banen,kamptid):
    sek_paa_banen_totalt = ant_paa_banen * kamptid*60 #antar at kamptid er gitt i minutt
    spilletid_per_pers = sek_paa_banen_totalt / ant_paa_laget
    benken_tid = int((sek_paa_banen_totalt/ant_paa_banen)-spilletid_per_pers)
    return benken_tid

def minutt_sekund(sekunder):
    minutt = sekunder//60
    kun_sekund = sekunder %60
    if kun_sekund <10:
        return f'{minutt}:0{kun_sekund}'
    else:
        return f'{minutt}:{kun_sekund}'

def les_inn_forfall():
    forfall_liste = []
    print('Skriv navn, eller kun ENTER (tom tekst) for å avslutte.')
    navn = input('Spiller som har meldt forfall: ')
    while navn != '':
        forfall_liste.append(navn)
        navn = input('Spiller som har meldt forfall: ')
    return forfall_liste

def finn_tilgjengelige(alle, forfall):
    ny_alle = []
    for i in range(len(alle)):
        ny_alle.append(alle[i])
    for j in forfall:
        ny_alle.remove(j)
    return ny_alle

import random
def laginndeling(spillere, sp_pr_lag):
    totalt_antall = len(spillere)
    antall_lag = totalt_antall//sp_pr_lag
    spillere_bestemt_lag = {} #dictionary med hvor mange spillere lag 1,2,3 osv skal ha
    for i in range(antall_lag):
        spillere_bestemt_lag[i] = sp_pr_lag 
    personer_ekstra = totalt_antall % sp_pr_lag
    while personer_ekstra > 0:
        for i in range(antall_lag):
            spillere_bestemt_lag[i] += 1
            personer_ekstra -=1 #legger inn en spiller ekstra til et lag til alle er fordelt
            if personer_ekstra == 0:
                break
    
    ny_spillere = []
    for i in range(len(spillere)):
        ny_spillere.append(spillere[i])

    lagliste = []
    for i in range(antall_lag):
        lagliste.append([])
    for key,val in spillere_bestemt_lag.items():
        for i in range(val):
            spiller = random.choice(ny_spillere)
            ny_spillere.remove(spiller)
            lagliste[key].append(spiller)
    return lagliste

sp = ['Ada', 'Bo', 'Eli', 'Isa', 'Cindy', 'Henrik',  'Ine', 'Jo', 'Kim', 'Lucas', 'My', 'Noor',  'Ola', 'Pia']
print(laginndeling(sp, 3))

BARN = ['Pia', 'Bo', 'Ada', 'Lucas', 'Emma A.', 'Cindy', 'Emma B.', 'Yngve', 'Ola', 'My', 'Quentin', 'Sara', 'Noor', 'Kim', 'Tuva', 'Rashad', 'Ine', 'Jo', 'Henrik']

def main():
    forfall_liste =  les_inn_forfall()

    sp_pr_lag = int(input('Spillere per lag: '))

    spillere = finn_tilgjengelige(BARN, forfall_liste)

    lagliste = laginndeling(spillere, sp_pr_lag)

    antall_lag = len(lagliste)

    kamptid = int(input('Kamptid (minutter): '))

    for i in range(antall_lag):
        print(f'Lag {i+1}:')
        antall_spillere = len(lagliste[i])
        print(lagliste[i])
        sekunder = sek_paa_benken(antall_spillere , sp_pr_lag , kamptid)
        sek_min = minutt_sekund(sekunder)
        print(f'Tid på benken per spiller: {sek_min}')

main()

def ny_fil(lagnavn, frafil, tilfil):
    f = open(frafil, 'r')
    t = open(tilfil, 'w')
    for linje in f:
        linjeliste = linje.split()
        if linjeliste[1] == lagnavn or linjeliste[4] == lagnavn:
            t.write(linje)
    f.close()
    t.close()
    return tilfil
