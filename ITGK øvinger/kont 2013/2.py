def yatzi(t1,t2,t3,t4,t5):
    terningkast = [t1,t2,t3,t4,t5]
    terningkast.sort()
    if terningkast[0]<1:
        return 'Ikke input verdier mindre enn 1!'
    elif terningkast[4]>6:
        return 'Ikke input verdier større enn 6!'
    return terningkast

def maxi_yatzi(liste):
    oppteller =[]
    for i in range(len(liste)+1):
        oppteller.append(0)
    for j in range(len(liste)):
        oppteller[liste[j]] += 1
    flest_av = 1
    for s in range(1,len(oppteller)):
        if oppteller[s] >= oppteller[flest_av]:
            flest_av = s
    return f'Du kastet {len(liste)} terninger og fikk flest {flest_av} ({oppteller[flest_av]} like).'