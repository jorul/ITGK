from math import*
gitt_tall = int(input('Skriv inn et positivt heltall: '))
dividert_tall = gitt_tall
høyeste_tall = int(round((gitt_tall)/2))+1
if gitt_tall == 0 or gitt_tall ==1:
    print(f'{gitt_tall} kan ikke primtallsfaktoriseres')
elif gitt_tall <0:
    print(f'Æ sa positivt heltall din fjottsækk. {gitt_tall} e itj nå positivt det.')


aktuelle_primtall = []
for muligprimtall in range(2, høyeste_tall):
    
    # Assume number is prime until shown it is not. 
    isPrime = True
    for divisor in range(2, muligprimtall):
        if muligprimtall % divisor == 0:
            isPrime = False
            break
      
    if isPrime:
        aktuelle_primtall.append(muligprimtall) #gir en liste med alle primtall mindre enn gitt_tall


faktor = 0
i=0
primtallsfaktorer = []
while i<len(aktuelle_primtall):
    rest = dividert_tall % aktuelle_primtall[i]
    if rest == 0:
        dividert_tall = dividert_tall/aktuelle_primtall[i]
        primtallsfaktorer.append(aktuelle_primtall[i]) #legger til primtallsfaktorer i liste
    elif rest != 0:
        i = i+1
    if dividert_tall == 1:
        break
if gitt_tall < 2:
    print('')
elif not primtallsfaktorer:
    print(f'{gitt_tall} er et primtall')
#print(gitt_tall,' = ', str(primtallsfaktorer.strip('[])')))
else:
    print ('Primtallsfaktorisering: ', gitt_tall, '=', ' * '.join(map(str, primtallsfaktorer)))