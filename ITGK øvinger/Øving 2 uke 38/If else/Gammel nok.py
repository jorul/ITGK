alder = int(input('Skriv inn din alder: '))
if alder >= 18:
    print('Du kan stemme både ved lokalvalg og Stortingsvalg.')
elif alder >= 16:
    print('Du kan stemme ved lokalvalg, men ikke ved Stortingsvalg.')
else:
    print('Du kan ikke stemme ennå.')