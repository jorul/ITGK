stoff = input('Si et stoff du er i besittelse av: ')
molar_masse = float(input('Hva er molvekt i gram for ' + stoff + '? '))
masse = float(input('Hvor mange gram ' + stoff + ' har du? '))

molekyler = (masse/molar_masse)*(6.022e23)

print('Du har', format(molekyler, '.1e'),'molekyler', stoff)


