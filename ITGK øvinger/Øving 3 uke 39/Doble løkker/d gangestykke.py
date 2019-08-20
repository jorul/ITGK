from random import*
kjøre = '1'
while kjøre == '1':
    tall1 = randint(0,9)
    tall2 = randint(0,9)
    riktigsvar = tall1*tall2

    print(riktigsvar)
    svaret = int(input(f'Hva er {tall1}*{tall2}? '))
    for i in range(0,3):
        if svaret == riktigsvar:
            print('Gratulerer det er helt riktig')
            kjøre = input('Er det ønskelig med flere spørsmål? skriv 1 for ja og 0 for nei ')
            break   
        elif  i == 2:
            print(f'Desverre ikke riktig. du har 0 forsøk igjen')
            print('Desverre klarte du ikke regnestykket, men vent du får et nytt et :)')
            kjøre = input('Er det ønskelig med flere spørsmål? skriv 1 for ja og 0 for nei ')   
        else:
            print(f'Desverre ikke riktig. du har {2-i} forsøk igjen')
            svaret = int(input(f'Hva er {tall1}*{tall2}? '))
if kjøre == '0':
    print('Ok, takk for nå.')
else:
    print('')
    print('Det var ikke et alternativ.')
    input('Her er et nytt stykke bare fordi du svarte teit: Hva er 58349254*354325432? ')
    print('Kan hende det var riktig, sannsynligvis var det feil. Hade, gidder ikke snakke med deg lengre.')