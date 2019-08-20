import random
print('Wilkommen zu Leithes Casino!')
print('Hier soll du eine Zahl geraten. Falls deine Antwort Richtig sind, wird du 500 Euro gewinnen.')
print('Falls deine Antwort Falsch sind, muss du Leithes Casino 100 Euro geben.')
print('Viel Glück!')
bunn = int(input('Anführen die unter-Grenze: '))
topp = int(input('Anführen die ober-Grenze: '))
tall = random.randint(bunn, topp)
pengertapt = []
i = 0
for i in range(topp-bunn+10000):
    svar = int(input('Rat ein Zahl: '))
    if svar>tall:
        print('Die Antwort ist zu gross.')
        pengertapt.append(-100)
    elif svar <tall:
        print('Die Antwort ist zu niedrig.')
        pengertapt.append(-100)
    elif svar == tall:
        pengertapt.append(500)
        print(f'RICHTIG! Du hast {i+1} Versuche benutzen.')
        print(f'Du hast jetzt {sum(pengertapt)} Euro.')
        break
# svar = int(input('Make a guess: '))
# while svar != tall:
#     svar = int(input('Make a guess: '))
# print(f'Riktig, svaret var {tall} du brukte ')