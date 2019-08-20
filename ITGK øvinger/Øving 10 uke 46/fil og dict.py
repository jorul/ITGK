import random
with open('biletter.txt','w') as file:
    personer = ['Vegard','Borge','Kari']
    for i in range (15):
        antall_biletter = str(random.randint(1,5))
        hvem = random.choice(personer)
        file.write(hvem + ',' + antall_biletter + '\n')

#Hvor mange har hver person kjøpt?

per_pers = {}

with open('biletter.txt','r') as file: # kan bruke 'try', 'Except filerror' elns :/
    for linje in file.readlines(): 
        linje = linje.strip().split(',') #.strip() fjerner tabs mellomrom og linjeskift
        navn = linje[0]
        antall_biletter = int(linje[1])
        if navn in per_pers.keys(): #Trenger ikke ha med '.keys()', '.values()
            per_pers[navn] += antall_biletter
        else:
            per_pers[navn] = antall_biletter
        # try, except KeyError

print(per_pers)


