def chess_match():
    total_score1 = 0
    total_score2 = 0
    num_games = input('Hvor mange partier skal spilles i kampen? ')
    if num_games < 1:
        print('Så kjedelig, da blir det ingen kamp!')
        return None
    else:
        for i in range(1,num_games+1):
            print(f'Parti {i}')
            score1 = float(input('Antall poeng til spiller 1 i partiet: '))
            score2 = float(input('Antall poeng til spiller 2 i partiet: '))
            total_score1 += score1
            total_score2 += score2
        print('Kampen er slutt!')
        print(f'Spiller 1 fikk {total_score1} poeng')
        print(f'Spiller 2 fikk {total_score2} poeng')

def end_of_match(num_games, game, total_score1,total_score2):
    vinnerpoeng = num_games/2 + 0.5
    if total_score1 >= vinnerpoeng:
        return 1
    elif total_score2>= vinnerpoeng:
        return 2
    elif game == num_games:
        return 3
    else:
        return 0

def chess_scorer():
    mulige_resultat = [0,0.5,1]
    score1 = input('Hvor mange poeng fikk spiller 1 i partiet?')
    while resultat not in mulige_resultat:
        print('Umulig resultat')
        score1 = input('Hvor mange poeng fikk spiller 1 i partiet?')
    score2 = 1-score1
    return score1,score2
    
def player_score(results):
    score = 0
    for i in results:
        if i != None:
            score += i
    return score