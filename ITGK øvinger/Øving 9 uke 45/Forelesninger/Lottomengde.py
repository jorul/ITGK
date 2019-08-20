vinnertall = {1,5,10,15,20,25,30}

mine_tall ={0}
for i in range(7):
    mine_tall.add(int(input('Skriv et tall: ')))


def sjekke_rekke(gjett, vinnertall):
    riktige = gjett.intersection(vinnertall)
    return len(riktige)

print(sjekke_rekke(mine_tall,vinnertall))

for item in liste:
    freq[item] = freq(item,0)+1

