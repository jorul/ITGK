svar = 'ingenting'
forsok = 0
while svar != '8':
    svar = input('Hvor mange bits er i en byte? ')
    forsok += 1
    if svar != '8':
        print('Det var feil, prøv igjen.')
print(f'Korrekt!! Du brukte {forsok} forsøk')