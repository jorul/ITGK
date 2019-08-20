def enterWords():
    wordList = []
    word = input('Enter word [Press Enter to quit]: ')
    while word != '':
        wordList.append(word)
        word = input('Enter word [Press Enter to quit]: ')
    return wordList

def noVowels(inList):
    vowels =['a','e','i','o','u','y']
    nylist = []
    for i in range(len(inList)):
        nyttord = ''
        for bokstav in range(len(inList[i])):
            if inList[i][bokstav] not in vowels:
                nyttord += inList[i][bokstav]
        nylist.append(nyttord)
    return nylist

import random
def randomSequence(listOne, listTwo):
    posisjoner = []
    newlistOne = []
    newlistTwo = []
    for i in range(len(listOne)):
        posisjoner.append(i)
    for s in range(len(listOne)):
        verdi = random.choice(posisjoner)
        posisjoner.remove(verdi)
        newlistOne.append(listOne[verdi])
        newlistTwo.append(listTwo[verdi])
    return (newlistOne, newlistTwo)

def printNewLines(number):
    for i in range(number-1):
        print()

def playGame(anwser,puzzles):
    poeng = 0
    for i in range(len(puzzles)):
        print(f'Puzzle word: {puzzles[i]}')
        guess = input('Guess word? ')
        if guess == anwser[i]:
            poeng +=1
            print('You anwsered correctly!')
        else:
            print(f'You anwsered incorrectly! The anwser should be {anwser[i]}')
    return poeng


print('The no Vowels Game')
print('===================================')
print('Player 2: Look away from the screen')
print('Player 1: Write in a list of English words in lower-case.')
wordList = enterWords()
noVowelsList = noVowels(wordList)
(anwsers, quizzes) = randomSequence(wordList, noVowelsList)
printNewLines(50)
print('Player 2: Guess words that lack all vowels:')
points = playGame(anwsers,quizzes)
print(f"You've got {points} of {len(anwsers)} points")