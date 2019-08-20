def les_inn_bilinfo():
    merke = input('Hvilket bilmerke var det? ')
    modell = input('Hvilken modell? ')
    farge = input('Hvilken farge? ')
    return [merke, modell, farge]

def sjekk_bil(vitne, bil):
    for i in range(3):
        if vitne[i] != '?': #hvis vitne ikke vet er det fortsatt 'True'
            if bil[i] != vitne[i]: # hvis de er ulike er det 'False
                return False
    return True


SKILTTALL = [1,2,3,4,5,6,7,8,9]
def les_gyldig_vitneskilt():
    gyldig_skilt = False
    gyldig_lengde = False
    gyldige_bokstaver = 0
    gyldige_tall = 0
    while gyldig_skilt == False:
        skilt = input('Skriv inn skilt, 2 bokst + 5 tall: ')
        skilt_liste = list(skilt)
        if len(skilt_liste) ==7:
            gyldig_lengde = True
        for j in range(2):
            if skilt_liste[j] == '?':
                gyldige_bokstaver +=1
            elif skilt_liste[j] in SKILTBOKSTAVER:
                gyldige_bokstaver +=1
        for i in range(2,7):
            if skilt_liste[i] == '?':
                gyldige_tall +=1
            elif int(skilt_liste[i]) in SKILTTALL:
                gyldige_tall +=1
        if gyldig_lengde == True and gyldige_bokstaver == 2 and gyldige_tall == 5:
            gyldig_skilt = True
        else:
            gyldig_lengde = False
            gyldige_bokstaver = 0
            gyldige_tall = 0
    return skilt

def match(vitne,bil):
    for i in range(7):
        if vitne[i] != '?': #hvis vitne ikke vet er det fortsatt 'True'
            if bil[i] != vitne[i]: # hvis de er ulike er det 'False
                return False
    return True

def match_liste(vitne, bil_liste):
    kan_stemme =[]
    for i in bil_liste:
        if match(vitne,i) == True:
            kan_stemme.append(i)
    return kan_stemme


def main():
    try:
        f = open('biler.txt','r')
        dict_biler ={}
        for linje in f:
            linje = linje.strip()
            linje_liste = linje.split(' ')
            dict_biler[linje_liste[0]] = linje_liste[1:]
        f.close()
        print('fil lest')
    except:
        print('An error occured.')
        return None
    keep_going = 'J'
    while keep_going == 'J':
        bilinfo_liste_fra_vitne = les_inn_bilinfo()
        skilt_fra_vitne = les_gyldig_vitneskilt()
        alle_skilt = []
        for key in dict_biler.keys():
            alle_skilt.append(key)
        skilt_som_stemmer = match_liste(skilt_fra_vitne, alle_skilt)
        biler_som_stemmer = []
        for i in skilt_som_stemmer:
            bilinfo = dict_biler[i][:3]
            if sjekk_bil(bilinfo_liste_fra_vitne, bilinfo) == True:
                biler_som_stemmer.append(i)
        if len(biler_som_stemmer)!= 0:
            print('Mulige kjøretøy er: ')
            for j in range(len(biler_som_stemmer)):
                eier = dict_biler[biler_som_stemmer[j]]
                print(f'{i} Eier: {eier[3]}')
        else:
            print('Ingen Match')
        keep_going = input('Vil du sjekke flere kjøretøyer? (J/N) ')