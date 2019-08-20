print('Tallkonvertering')
print()
print('oppgave a)')

flyt1 = float(input('Skriv inn et flyttall: '))
flyt2 = float(input('Skriv inn enda et flyttall: '))
flyt3 = float(input('Skriv inn et siste flytall: '))
print()
print('konvertert til heltall blir det:', int(flyt1), int(flyt2), int(flyt3))
print()

heltall = input('skriv inn et heltall ')
print ('Konvertert til flyttall blir det',float(heltall))

print()
print()


print('oppgave b)')

navn = input('Skriv ditt navn: ')
alder = input('Hei ' + navn + ' hvor gammel er du? ')
prog = input('hvor gammel var du da du begynte å programmere? ')
diff = int(alder) - int(prog)
print('Da har du programmert i', diff, 'år.')
svar = input('Synes du de ' + str(diff) + ' årene har vært givende? ')
print('Takk for svar', navn)

print()
print()

print('oppgave c)')

print('Vennligst gi inn et flyttall med minst 5 siffer både før og etter .')
hel = input('Hva er tallet ditt?')
print('konvertert med heltall med int():', int(hel))



