import random
def throw(n):
    terningøyne = [1,2,3,4,5,6]
    kast =[]
    for i in range(n):
        kast.append(random.choice(terningøyne))
    return kast

def chance(dice):
    summen = 0
    for i in range(len(dice)):
        summen += dice[i]
    return summen

def house(dice):
    verdi1 = dice[0]
    verdi2 = dice[1]
    s = 2
    while verdi2 == verdi1: #skal være to ulike verdier
        verdi2 = dice[s]
        s+=1
        if s==5:
            return 0 #Skjer dersom alle elementene er like
    
    antall_verdi1 = 0
    for i in range(len(dice)): #teller antall av verdi1
        if verdi1 == dice[i]:
            antall_verdi1 +=1
    
    antall_verdi2 = 0
    for i in range(len(dice)): #teller antall av verdi2
        if verdi2 == dice[i]:
            antall_verdi2 += 1

    if (antall_verdi1 == 3 and antall_verdi2 ==2) or (antall_verdi1 == 2 and antall_verdi2 ==3):
        return chance(dice)
    else: 
        return 0 # ikke 2+3 like

def straight(dice):
    dice.sort() #sorterer lista
    ok = 0
    for i in range(1,5):
        if dice[i]== (dice[i-1] +1): #sjekker om neste element er 1 større enn forrige
            ok +=1
    if ok ==4:
        if dice[0]==1:
            return 15
        elif dice[0]==2:
            return 20
    else:
        return 0