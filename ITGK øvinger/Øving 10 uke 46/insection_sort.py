def sorting(liste):
    for s in range(1,len(liste)):
        verdi = liste[s]
        hull = s
        for t in range(s-1,-1,-1):
            if verdi < liste[t]:
                hull = t
                liste[t+1] = liste[t]
        liste[hull] = verdi
    return liste

print(sorting([1,5,9,2,7,3,8,10]))
