def isTautonym(ord):
    splittet = ord.split(' ')
    if len(splittet) <2:
        return False
    antall_like = 0
    for i in range(len(splittet)):
        if splittet[i].lower() == splittet[1].lower():
            antall_like += 1
    if antall_like == len(splittet):
        return True
    return False

print(isTautonym('Bubo bubo bubo'))

def num_el(el, lst):
    antall = 0
    for element in lst:
        if element == el:
            antall +=1
    return antall

def remove_duplicates(lst):
    liste_med_unike =[]
    indexer_som_skal_bort= []
    for i in range(len(lst)):
        if lst[i] in liste_med_unike:
            indexer_som_skal_bort.append(i)
        else:
            liste_med_unike.append(lst[i])
    indexer_som_skal_bort.reverse()
    for index in indexer_som_skal_bort:
        lst.pop(index)
    return lst


print(remove_duplicates([1,2,3,1,4,5,4,3,6,7,8,7,9]))

def sorted_list(words):
    orginal = words.split()
    new = []
    for el in orginal:
        new.append(el.lower())
    newnew = sorted(new)
    skal_returneres =[]
    for i in newnew:
        for j in orginal:
            if j.lower()== i:
                skal_returneres.append(j)
    return skal_returneres

words = "Dette Er et FLOTT eksempel Med små og STORE bokstaver."
print(sorted_list(words))


def has_length(capitals, length):
    riktig = []
    for city in capitals:
        if n_letters(city)==length:
            riktig.append(city)
    return riktig

import random
def length_question(capitals):
    mulige_lengder = []
    for city in capitals:
        if n_letters(city) not in mulige_lengder:
            mulige_lengder.append(n_letters(city))
    lengde= random.choice(mulige_lengder)
    svar = has_length(capitals,lengde)
    return f'Capital with {lengde} letters?', svar

def play_quiz(capitals):
    Wannaplay = True
    poeng = 0
    while Wannaplay == True:
        q, s = random_question(capitals)
        svar = input(q)
        if svar == 'Q':
            Wannaplay = False
        elif svar in s:
            poeng +=1
            print('Correct!')
        else:
            print('Sorry, that was wrong!')
    return poeng

def main():
    print('CAPITALS QUIZ')
    print('Answer questions to score points')
    print('To quit, answer Q')
    poeng = play_quiz(CAPITALS)
    if poeng ==1:
        print('Congrats! you scored 1 point!')
    else:
        print(f'Congrats! you scored {poeng} points!')

def pytagoreanTriplets(n):
    listami = []
    k = 10
    while len(listami) < n:
        for a in range(1,k):
            for b in range(1,k**2):
                for c in range(1,k**2):
                    if a**2+b**2 == c**2:
                        if [a,b,c] not in listami and [b,a,c] not in listami:
                            listami.append([a,b,c])
        k+=10
    return listami

print(pytagoreanTriplets(10))