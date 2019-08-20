ant1 = float(input('Hvor mange cookies vil du lage? '))
ant2 = float(input('Hvor mange cookies vil du lage nå? '))
ant3 = float(input('Hvor mange cookies vil du lage til slutt? '))



print('Antall cookies'.rjust(15) + 'sukker (g)'.rjust(15) + 'sjokolade (g)'.rjust(15))
print(str(int(ant1)).rjust(15) + str(round(400*(ant1)/48, 1)).rjust(15) + str(round(500*(ant1)/48,1)).rjust(15))
print(str(int(ant2)).rjust(15) + str(round(400*(ant2)/48, 1)).rjust(15) + str(round(500*(ant2)/48,1)).rjust(15))
print(str(int(ant3)).rjust(15) + str(round(400*(ant3)/48, 1)).rjust(15) + str(round(500*(ant3)/48,1)).rjust(15))


