def cold_days(templist):
    days = 0
    for i in templist:
        if i<0:
            days += 1
    return days

def cap_data(array,min_value, max_value):
    resultat = []
    for i in range(len(array)):
        if array[i] < min_value:
            resultat.append(min_value)
        elif array[i] > max_value:
            resultat.append(max_value)
        else:
            resultat.append(array[i])
    return resultat

import random
def generate_testdata(N, min_value, max_value):
    nyliste = []
    while len(nyliste)<N:
        tall = random.randint(min_value,max_value)
        if tall not in nyliste:
            nyliste.append(tall)
    return nyliste

def create_db(temp, rain, humidity,wind):
    weather ={}
    for dag in range(len(temp)):
        dagData = [temp[dag], rain[dag], humidity[dag], wind[dag]]
        weather[dag+1] = dagData
    return weather

def print_db(weather):
    print('Day | Temp | rain | humidity | wind')
    print('====+======+======+==========+======')
    for keys in weather.keys():
        print(str(keys).rjust(4), str(weather[keys][0]).rjust(6), str(weather[keys][1]).rjust(6), str(weather[keys][2]).rjust(10), str(weather[keys][3]).rjust(6))
temp = [1,5,3]
rain = [0,30,120]
humidity = [30,50,65]
wind = [3,5,7]
weather = create_db(temp,rain,humidity,wind)
print(weather)
print_db(weather)

def strange_weather(temp,rain):
    start = 0
    stop = 0
    antall_dager = 0
    midlertidig_start = 0
    midlertidig_stop = 0
    midlertidig_dager = 0
    if temp[0] <0:
        midlertidig_start = 1
        midlertidig_stop = 1
        midlertidig_dager = 1
        start = 1
        stop = 1
        antall_dager = 1

    for i in range(1,len(temp)):
        if midlertidig_dager > antall_dager:
            start = midlertidig_start
            stop = midlertidig_stop
            antall_dager = midlertidig_dager
        if temp[i]<0:
            if midlertidig_start ==0:
                midlertidig_start = i+1
                midlertidig_stop = i+1
                midlertidig_dager = 1
            elif rain[i]>rain[i-1] and temp[i]<temp[i-1]:
                midlertidig_stop = i+1
                midlertidig_dager +=1
            else:
                if midlertidig_dager != 0:
                    midlertidig_start = 0
                    midlertidig_stop = 0
                    midlertidig_dager = 0
        else:
            if midlertidig_dager != 0:
                midlertidig_start = 0
                midlertidig_stop = 0
                midlertidig_dager = 0
    return(start,stop)

temp=[1,3, 4, -5,-6,-7,-8,-9,3,0]
rain=[0,20,30,0,10,30,50,0,5,2]
(start, stop) = strange_weather(temp,rain)
print(start, stop)
