import random

numbers =[]
for i in range (1,35):
    numbers.append(i)

def drawNumbers(n):
    return random.sample(numbers,n)

def compList(nr1, nr2):
    like_tall = 0
    for i in range (len(nr1)):
        for p in range (len(nr2)):
            if nr1[i] == nr2[p]:
                like_tall +=1
    return like_tall

def Winnings(rette,tillegg):
    if rette == 7:
        return 2749455
    elif rette == 6 and tillegg >= 1:
        return 102110
    elif rette == 6:
        return 3385
    elif rette == 5:
        return 95
    elif rette == 4 and tillegg >= 1:
        return 45
    else:
        return 0

def main():
    myGuess = drawNumbers(7)
    Lottotall = drawNumbers(10)
    Tilleggstall = []
    for i in range (3):
        Tilleggstall.append(Lottotall[i])
        Lottotall.pop(i)
    like_lotto = compList(myGuess, Lottotall)
    like_tillegg = compList(myGuess, Tilleggstall)
    #print(myGuess)
    #print(Lottotall)
    #print(Tilleggstall)
    #print(like_lotto)
    #print(like_tillegg)
    tjent = Winnings(like_lotto, like_tillegg)-5
    return tjent

tjent = 0
for i in range (1000000):
    tjent += main()
    if i%10000==0:
        print(tjent)


# etter å ha spilt 1 000 000 ganger: -3 846 555 kr :(