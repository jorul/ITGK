print('INFO')
print('Dette programmet besvarer om din utleie en annen type bolig,')
print('her sekundær- eller fritidsbolig, er skattepliktig.')
print('Først trenger vi å vite om du leier ut en sekundær- eller en fritidsbolig.')
print('---------------------------------------------------------------------')
print('DATAINNHENTING:')
bolig = str.lower(input('Skriv inn type annen bolig (sekundærbolig/fritidsbolig) du har leid ut: '))
if bolig == 'fritidsbolig':
    print('\nINFO')
    print(f'Du har valgt {bolig}.')
    print(f'Nå trenger vi først å vite om {bolig}en(e) primært brukes til utleie eller fritid. \nDeretter trenger vi å vite hvor mange {bolig}(er) du leier ut. \nTil slutt trenger vi å vite hvor store utleieinntekter du har pr. {bolig}.')
print('\n---------------------------------------------------------------------')
print('DATAINNHENTING:')
if bolig == 'fritidsbolig':
    formål = str.lower(input('Skriv inn formålet med fritidsboligen(e): '))
antall = int(input(f'Skriv inn antallet {bolig}er du leier ut: '))
inntekt = int(input(f'Skriv inn utleieinntekten pr. {bolig}: '))
print('\n--------------------------------------------------------------------- \nSKATTEBEREGNING:')
if bolig == 'sekundærbolig' or (bolig == 'fritidsbolig' and not formål == 'fritid') or (bolig == 'fritidsbolig' and formål== 'fritid' and inntekt>10000):
    print('Inntekten er skattepliktig')
    if bolig == 'sekundærbolig' or (bolig == 'fritidsbolig' and not formål == 'fritid'):
        print(f'Totalt skattepliktig beløp er {inntekt*antall}')
    else:
        print(f'Overskytende beløp pr. fritidsbolig er {inntekt-10000}')
        print(f'Skattepliktig inntekt pr. fritidsbolig er {(inntekt-10000)*0.85}')
        print(f'Totalt skattepliktig beløp er {(inntekt-10000)*0.85*antall}')
else:
    print('Inntekten er ikke skattepliktig')