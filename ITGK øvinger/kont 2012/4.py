def pulsStatistikk(pulsData):
    sortert = []
    sum = 0
    for i in range(len(pulsData)):
        sortert.append(pulsData[i])
        sum += pulsData[i]
    sortert.sort()
    gjennomsnitt = round(sum/(len(pulsData)),2)
    return[gjennomsnitt, sortert[0], sortert[len(sortert)-1]]

def pulsSoneGrenser(makspuls):
    grenser_p = [0.6,0.725,0.825,0.875,0.925]
    grenser = []
    for i in range(5):
        grenser.append(round(grenser_p[i]*makspuls,1))
    return grenser

print(pulsSoneGrenser(188))

def pulssoner(makspuls,pulsData):
    grenser = pulsSoneGrenser(makspuls)
    soner = [0,0,0,0,0]
    for i in pulsData:
        if i>=grenser[4]:
            soner[4] +=1
        elif i>=grenser[3]:
            soner[3] += 1
        elif i>=grenser[2]:
            soner[2] += 1
        elif i>=grenser[1]:
            soner[1] +=1
        elif i>=grenser[0]:
            soner[0] +=1
    
    for i in range(5):
        soner[i] = round(100*soner[i]/len(pulsData))
    return soner

pulser = [110,118,125,127,127,130,129,131,132,134,134,135,145,157,165,172,173,178,179,178]

print(pulssoner(188,pulser))

def lengstePulsOkning(pulsData):
    start = 1 #starter med at sek 1 gir lengste interval
    lengde = 1
    midl_start = 1 
    midl_lengde = 1
    for i in range(1,len(pulsData)): 
        if pulsData[i]>= pulsData[i-1]: #lengden økes med en dersom puls har økt
            midl_lengde +=1
            if midl_lengde> lengde: #hvis lengden nå er lengre enn tidligere målte lengste lengde
                lengde = midl_lengde
                start = midl_start
        else:
            midl_lengde = 1 #begynner tellingen på nytt
            midl_start = i+1
    return[lengde,start]
print(lengstePulsOkning(pulser))
