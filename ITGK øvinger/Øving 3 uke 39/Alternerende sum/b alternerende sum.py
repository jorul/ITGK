k = int((input('k = ')))
tall = 0
t=0
i = 1
while tall<=k:
    rest = i%2
    if rest == 0:
        t = -i**2
    else:
        t = i**2
    if tall + t > k:
        break
    tall = tall + t
    i = i+1
#tall = tall - t
print(f'summen av tallene før summen blir større enn {k} er {tall}. Antall iterasjoner: {i-1}')