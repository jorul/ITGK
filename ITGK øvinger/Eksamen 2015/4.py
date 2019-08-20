NTNU_scores = (89,77,65,53,41,0)
NTNU_letters = ('A','B','C','D','E','F')
TASKS = ('1','2a','2b','2c','3a','3b','3c','3d','4a','4b','4c','4d','4e','4f','4g','4h')
WEIGHTS = (25,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5)

def makeArray(Numbers, Text):
    nyliste = []
    for i in range(len(Numbers)):
        nyliste.append([Numbers[i], Text[i]])
    return nyliste

def computeScore(Points, weights):
    poeng = 0
    for i in range(len(Points)):
        poeng += Points[i]*weights[i]/10
    return poeng

def score2Letter(scoreSum,limitLetters):
    for i in range(len(limitLetters)):
        if scoreSum >= limitLetters[i][0]:
            return limitLetters[i][1]

def addCandidate(candidateNumber, Scores, weights):
    try:
        f = open('eksamen.txt', 'w+')
        score = computeScore(Scores, weights)
        f.write(candidateNumber, end = '\t')
        for i in range(len(Scores)):
            print(Scores[i], end = '\t')
        print(score)
        f.close()
    except Exception as errorMessage:
        print(errorMessage)


def readResultFile(filename):
    f = open(filename, 'r')
    listami = []
    for linje in f:
        liste = linje.split('\t')
        listami.append(liste)
    for i in range(len(listami)):
        for s in range(len(listami[i])-1):
            listami[i][s] = int(listami[i][s])
        listami[i][len(listami[i])-1] = float([len(listami[i])-1])
    return listami

def checkResultOK(filename, weights):
    f = open(filename, 'r')
    total_liste = readResultFile(filename)

    krav1 = True
    krav2 = True
    krav3 = True

    for i in range(len(total_liste)):
        for j in range(i+1,total_liste):
            if total_liste[i][0] == total_liste[j][0]:
                print(f'ERROR: Candidate {total_liste[i][0]} appears more than once!')
                krav1 = False
    
    for s in range(len(total_liste)):
        for t in range(1,len(totalliste[i])-1):
            if total_liste[s][t] <0 or total_liste[s][t] >10:
                print(f'ERROR: Candidate {total_liste[i][0]} scores are not between 0-10!')
                krav2 = False
    
    for u in range(len(total_liste)):
        score_egentlig = computeScore(total_liste[u][1:len(totalliste[i])-1], weights)
        if score_egentlig != total_liste[u][len(totalliste[i])-1]:
            print(f'ERROR: Candidate {total_liste[u][0]} has wrong total score!')
            krav3 = False
    if krav1 == True and krav2 == True and krav3 == True:
        return True
    else:
        return False

    

def checkResultOK2(total_liste, weights):

    krav1 = True
    krav2 = True
    krav3 = True

    for i in range(len(total_liste)):
        for j in range(i+1,len(total_liste)):
            if total_liste[i][0] == total_liste[j][0]:
                print(f'ERROR: Candidate {total_liste[i][0]} appears more than once!')
                krav1 = False
    
    for s in range(len(total_liste)):
        for t in range(1,len(total_liste[i])-1):
            if total_liste[s][t] <0 or total_liste[s][t] >10:
                print(f'ERROR: Candidate {total_liste[s][0]} scores are not between 0-10!')
                krav2 = False
    
    for u in range(len(total_liste)):
        score_egentlig = computeScore(total_liste[u][1:len(total_liste[u])-1], weights)
        if score_egentlig != total_liste[u][len(total_liste[u])-1]:
            print(f'ERROR: Candidate {total_liste[u][0]} has wrong total score!')
            krav3 = False
    if krav1 == True and krav2 == True and krav3 == True:
        return True
    else:
        return False

total_liste = [[12300,0,10,10,10,0,0,0,0,0,10,10,10,10,10,10,10,50.0],
[44400,4,4,11,0,0,0,0,0,0,0,0,0,0,0,0,0,19.0],
[12300,9,0,0,0,10,10,10,10,10,0,0,0,0,0,0,0,47.5]]

print(checkResultOK2(total_liste, WEIGHTS))
    

    