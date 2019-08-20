import random
def sjekk_vinner(spiller, dealer):
    sum_spiller = sum(spiller)
    sum_dealer = sum(dealer)
    # 1 betyr at dealer vinner, 0 betyr at spiller vinner
    if sum_spiller > 21:
        return ' '
    elif (spiller.count(1) or spiller.count(11)) and (spiller.count(10)):
        return ' '
    elif sum_dealer>21:
        return 0
    elif sum_spiller > sum_dealer:
        return 0
    else:
        return 1

def trekk(antall):
    mulige_kort = [2,3,4,5,6,7,8,9,10,10,10,11]
    a = []
    for i in range(antall):
         a.append(random.choice(mulige_kort))
    if sum(a)==22:
        a = [11,1]
    return a

def black_jack():
    dealerens_kort = trekk(2)
    spillerens_kort = trekk(2)
    score = sum(spillerens_kort)
    print(f'Dealers cards are {dealerens_kort[1]} and ?')
    print(f'Your score is {score}')
    nyrunde = input('Do you want another card? (J/N) ')
    while nyrunde == 'J':
        nyttkort = (trekk(1))
        if nyttkort == 11 and score + nyttkort > 21:
            nyttkort = 1
        spillerens_kort.extend(nyttkort)
        score = sum(spillerens_kort)
        if score > 21:
            print(f'You got: {score}')
            print('You lost')
            break
        elif ((1 in spillerens_kort) or (11 in spillerens_kort )) and (10 in spillerens_kort):
            print('EKTE BLACKJACK!')
            print('You won')
            break
        print(f'Your score is {score}')
        nyrunde = input('Do you want another card? (J/N) ')
    vinneren = sjekk_vinner(spillerens_kort, dealerens_kort)
    if vinneren == 1:
        print(f'Dealers score is: {sum(dealerens_kort)}')
        print('You lost')
    elif vinneren == 0:
        print(f'Dealers score is: {sum(dealerens_kort)}')
        print('You won')

black_jack()