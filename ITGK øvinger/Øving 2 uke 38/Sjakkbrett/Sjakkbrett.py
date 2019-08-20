linje = str.lower(input('linje: '))
tall = int(input('tall: '))
boksa = ['a', 'c', 'e', 'g']
boksb = ['b', 'd', 'f', 'h']
bokstaver = boksa + boksb
odde = [1,3,5,7]
par = [2,4,6,8]
tallene = odde + par
if linje not in bokstaver or tall not in tallene:
    print('Det der er ikke noen rute på et sjakkbrett din fjott!')
    print('Feil input. Første tegn må være en bokstav A-H eller a-h. Andre tegn må være et tall 1-8')
elif linje in boksa:
    if tall in par:
        print('hvit')
    elif tall in odde:
        print('svart')
elif linje in boksb:
    if tall in par:
        print('svart')
    elif tall in odde:
        print('hvit')