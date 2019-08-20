def check_highscore(points, scores):
    for i in scores.keys():
        if points>scores[i][1]:
            return i
    return -1

def print_highscores(scores):
    for i in range(1,len(scores)+1):
        print((str(i)).rjust(2), scores[i][0].ljust(20), (str(scores[i][1])).rjust(5))

def add_highscore(points, name, scores):
    plassering = check_highscore(points, scores)
    if plassering == -1:
        return scores
    #antall_flytt_nødvending = len(scores)-plassering
    for i in range(len(scores),plassering,-1): #begynner på 10, går nedover til den når plassering
        scores[i] = scores[i-1] #person på plass i-1 får en plassering lavere
    scores[plassering] = [name,points]
    return scores

def most_highscores(scores):
    navn_antall = 1
    navn = scores[1][0]
    for i in range(1,len(scores)+1):
        antall = 1
        for s in range (i+1,len(scores)+1):
            if scores[s][0] == scores[i][0]:
                antall +=1
        if antall > navn_antall:
            navn_antall = antall
            navn = scores[i][0]
    return navn

import random
def new_highscorelist():
    highscores = {}
    alle_navn = ['Albus','Fleur','Frank','Harry', 'Hermine', 'Minerva', 'Ron', 'Severus', 'Sirus','Vernon']
    scores = [100,90,80,70,60,50,40,30,20,10]
    for i in range(1,11):
        navn_plass = random.randint(0,len(alle_navn)-1)
        highscores[i] = [alle_navn[navn_plass],scores[i-1]]
        alle_navn.pop(navn_plass)
    return highscores


print_highscores(new_highscorelist())

