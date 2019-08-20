pizza = input('Pizza: ')
stud = input('Studentrabat: ')
tips = input('Tips: ')

print('Totalt =', float(pizza) - float(pizza)*float(stud)/100 + float(pizza)*float(tips)/100)

print()
print()

print('oppgave c)')
pris = input('Total pris: ')
pers = input('Hvor mange deltok på middagen? ')
print('Ettersom dere var', pers, 'personer, så må hver person betale', float(pris)/float(pers))
