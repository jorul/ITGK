def binaersøk(liste,verdi,mini,maks):
    if maks<mini:
        return 'Verdi ikke funnet'
    else:
        mid = (maks+mini)//2
        if verdi == liste[mid]:
            return mid
        elif liste[mid] < verdi:
            return binaersøk(liste,verdi,mid+1,maks)
        elif liste[mid] > verdi:
            return binaersøk(liste,verdi,mini,mid-1)

print(binaersøk([1,2,3,9,11,13,17,25,57,90],57,0,9))
