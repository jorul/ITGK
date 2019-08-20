def sjekk_svar(svar):
    poeng = 0
    fasit= ['A', 'C', 'B', 'D', 'A', 'A', 'B', 'A', 'C', 'A,', 'D', 'A', 'C', 'C', 'B', 'A', 'B', 'A', 'C', 'D']
    for i in range (len(svar)):
         if svar[i]==fasit[i]:
            poeng +=1
    return poeng*100/20
print(sjekk_svar(['A', 'C', 'B', 'D', 'A', 'A', 'B', 'A', 'C', 'A,', 'D', 'A', 'C', 'C', 'B', 'A', 'B', 'A', 'C', 'D']))
