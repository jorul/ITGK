def initElection(parties):
    antall_parti = len(parties)
    delliste = [0]* antall_parti
    fulliste = []
    for i in range(92):
        fulliste.append(delliste)
    return fulliste
parties = ['TeaParty','CoffeeParty','MilkParty','HouseParty','BeachParty']
election = initElection(parties)
print(election[:3])

def updateElection(valgdata, nr, stemmetall):
    for i in range(len(stemmetall)):
        valgdata[nr][i] += stemmetall[i]
    return valgdata



election = updateElection( election, 34, [123,3321,3442,23,1])
print(election[34])
election = updateElection( election, 34, [601,2000,3000,50,22])
print(election)

def sumvalgdata(valgdata):
    sumasjon = [0] * (len(valgdata[0]))
    for i in range(len(valgdata)):
        for j in range(len(sumasjon)):
            sumasjon[j] += valgdata[i][j]
    return sumasjon

def ledervalg(sumasjon):
    lederindex = 0
    for i in range(len(sumasjon)):
        if sumasjon[i]>sumasjon[lederindex]:
            lederindex = i
    return lederindex


def printLeadP(valgdata):
    sumasjon = sumvalgdata(valgdata)
    leder = ledervalg(sumasjon)
    print(f'{parties[leder]} is leading the election with {sumasjon[leder]} votes')

printLeadP(election)

def vinnerparti(valgdata, nr):
    lederindex = 0
    for i in range(len(valgdata[nr])):
        if valgdata[nr][i] > valgdata[nr][lederindex]:
            lederindex = i
    if valgdata[nr][lederindex] == 0: #hvis det med flest stemmer har fått null stemmer
        return 'no votes'
    for j in range(len(valgdata[nr])):
        if j != lederindex:
            if valgdata[nr][j] == valgdata[nr][lederindex]: # dersom et annet parti har fått like mange stemmer som det som har fått flest
                return 'tied'
    return parties[lederindex] #partiet med flest stemmer returneres

def getresults(valgdata):
    resultat = {}
    for i in parties:
        resultat[i] = 0
    resultat['tied'] = 0
    resultat['no votes'] = 0
    for i in range(len(valgdata)):
        delvinner = vinnerparti(valgdata, i)
        resultat[delvinner] +=1
    return resultat

def printresults(valgdata):
    resultat = getresults(valgdata)
    for key,val in resultat.items():
        print(key.ljust(20), end = '')
        print(str(val).ljust(4), end = ' ')
        if val == 1:
            print('delegate')
        else:
            print('delegates')

printresults(election)

