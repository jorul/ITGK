import datetime
def diff_date(start,end):
    d0 = datetime.date(start[0],start[1],start[2])
    d1 = datetime.date(end[0],end[1],end[2])
    delta = d1-d0
    return delta.days


def time_diff(start, slutt):
    dager_diff = diff_date(start[:3], slutt[:3])
    timer_diff = slutt[3]-start[3]
    min_diff = slutt[4]-start[4]
    sek_diff = slutt[5]-start[5]
    total_diff = dager_diff*24*60*60+timer_diff*60*60+min_diff*60 + sek_diff
    return total_diff


def check_min_distance(car_table,diff):
    crazy_drivers =[]
    for i in range(1,len(car_table)):
        avstand = time_diff(cartable[i-1][:6],cartable[i][:6])
        if avstand<diff:
            bilnr = cartable[i][6]
            crazy_drivers.append(bilnr)
    return crazy_drivers



def list_speeders(liste_a, liste_b,grense,distanse):
    speeders = []
    bilnr_dict = {}
    for element in liste_a:
        bilnr = element[6]
        bilnr_dict[bilnr] = [element[:6]] #liste men en liste i
    for belement in liste_b:
        bilnr = belement[6]
        bilnr_dict[bilnr].append(belement[:6])
        #dictonary med bilnr som key, og passeringene som lister i ei liste
        
    minimum_tidsbruk = (distanse/grense)*60*60 #gitt i sekunder
    for key,val in bilnr_dict.items():
        bilnr = key
        pass_a = val[0]
        pass_b = val[1]
        tidsbruk_i_sek = time_diff(pass_a, pass_b)
        if tidsbruk_i_sek < minimum_tidsbruk:
            speeders.append(bilnr)
    return speeders


liste_a = [[2017, 11, 17, 6, 21, 12, 'HB69082'], [2017, 11, 17, 6, 21, 53, 'CV86023'], 
[2017, 11, 17, 6, 23, 0, 'HD27560'], [2017, 11, 17, 6, 23, 2, 'UT29891'], 
[2017, 11, 17, 6, 24, 25, 'IS11293'], [2017, 11,17, 6, 24, 40, 'EL73840'], 
[2017, 11, 17, 6, 24, 41, 'UT55227'], [2017, 11, 17, 6, 26, 55, 'NB59108'], 
[2017, 11, 17, 6, 27, 29, 'UT46408'], [2017, 11, 17, 6, 28, 19, 'LE68228']]

liste_b = [[2017,11,17,6,31,15,'HB69082'],[2017,11,17,6,32,19, 'UT29891'],
[2017,11,17,6,32,40,'EL73840'],[2017,11,17,6,34,15, 'HD27560'],
[2017,11,17,6,35,45, 'IS11293'],[2017,11,17,6,36,30,'LE68228'],
[2017,11,17,6,36,15,'UT55227'],[2017,11,17,6,38,5,'NB59108'],
[2017,11,17,6,38,9,'UT46408'], [2017,11,17,6,41,59,'CV86023']]

speeders = list_speeders(liste_a, liste_b,60,10)
print(speeders)