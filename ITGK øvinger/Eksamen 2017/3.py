def file_to_table(filename):
    f = open(filename, 'r')
    helliste = []
    for linje in f:
        linjeliste = (line.strip()).split(',')
        for i in range(6):
            linjeliste[i] = int(linjeliste[i])
        helliste.append(linjeliste)
    f.close()
    return helliste


def time_diff(start, end):
    dato_start = start[:3]
    dato_slutt = end[:3]
    dager = diff_date(dato_slutt,dato_slutt) #Går ut i fra at diff_date faktisk returnerer antall dager MELLOM de to dagene - altså hvis bilen returnerer neste dag er det 0 fordi det er ingen dager mellom f.eks. 17. og 18.
    if dager == 0 and dato_start == dato_slutt:
        timer = end[3]- start[3]
        minutter = end[4] -start[4]
        sekunder = end[5] -start[5]
        summen = timer*60*60 + minutter*60 + sekunder
    else: 
        summen = dager*60*60*24 
        start_timer = 23 - start[3]
        start_minutter = 59 - start[4]
        start_sekunder = 60-start[5]

        summen += start_timer*60*60+start_minutter*60 + start_sekunder
        summen += end[3]*60*60 + end[4]*60 + end[5]
        
    return summen




def check_min_distance(car_table, diff):
    listami = []
    for i in range(1,len( car_table)-1):
        avstand = time_diff(car_table[i-1][:6], car_table[i][:6])
        if avstand < diff:
            listami.append(car_table[i][6])
    return listami

def list_el_cars(car_table):
    antall = 0
    for liste in car_table:
        reg_nr = liste[6]
        bokstaver = reg_nr[0:2]
        if bokstaver[0] == 'EK' or bokstaver[0] == 'EL' or bokstaver[0] == 'EV':
            antall += 1
    return antall

import random
def generate_license_numbers(amount):
    liste = []
    Bokstaver = ['BS', 'CV', 'EL', 'FY', 'KU', 'LE', 'NB', 'PC', 'SY', 'WC']
    i = 0
    while i < amount:
        nummeret = random.choice(Bokstaver) + str(random.randint(10000,99999))
        if nummeret not in liste:
            liste.append(nummeret)
            i +=1
    return liste

def list_speeders(filename_a, filename_b, speed_limit, distance):
    speeders = []
    minimum_tidsbruk = (distance/speed_limit)*60*60
    a = file_to_table(filename_a)
    b = file_to_table(filename_b)
    for liste_a in a:
        for liste_b in b:
            if liste_a[6] == liste_b[6]:
                tidsbruk = time_diff(liste_a[:6], liste_b[:6])
                if tidsbruk < minimum_tidsbruk:
                    speeders.append(liste_a[6])
    return speeders





A = 'Jorunn, er, en liten fis \n'
linjeliste = A.strip().split(',')
print (linjeliste)
print(linjeliste[:2])