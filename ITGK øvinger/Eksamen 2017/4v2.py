def konv(tall):
    if tall<10:
        return '0' + str(tall)
    else:
        return tall

def formatTime(seconds):
    hh = konv(seconds //3600)
    mm = konv((seconds %3600)//60)
    ss = konv((seconds %3600)%60)
    return f'{hh}:{mm}:{ss}'

def valuesDecember():
    first = 3*60*60+18*60
    period = 12*60*60+25*60+12
    return first, period

def genTides():
    første_lavvann, period = valuesDecember()
    lavvann= []
    høyvann = []
    lav_tid = første_lavvann
    while lav_tid <31*24*60*60:
        lavvann.append(lav_tid)
        lav_tid += period
    høy_tid = int(første_lavvann + 0.5*period)
    while høy_tid <31*24*60*60:
        høyvann.append(høy_tid)
        høy_tid += period
    return lavvann, høyvann

print(formatTime(12305))
lows,highs=genTides()
print(highs[:8])

def genTidesStr(tideList):
    liste =[]
    for element in tideList:
        dato = int(element)//(24*60*60) +1
        tidspunkt = int(element)%(24*60*60)
        tid_skrevet_fint = formatTime(tidspunkt)
        liste.append(f'{dato} {tid_skrevet_fint}')
    return liste

#kan kun være høyvann eller lavvann da eksamen varer kun 4 timer

def checkTides(dayInMonth):
    lows,highs = genTides()
    lowStrings = genTidesStr(lows)
    highStrings = genTidesStr(highs)
    resultat = 'no tides'
    for i in lowStrings:
        splitt = i.split(' ')
        dagen = splitt[0]
        tidspunkt = splitt[1].split(':')
        if int(tidspunkt[0])>=9 and int(tidspunkt[0])<=13:
            if int(dagen) == dayInMonth:
                resultat = f'low tide at {splitt[1]}'
    for s in highStrings:
        splitt = s.split(' ')
        dagen = splitt[0]
        tidspunkt = splitt[1].split(':')
        if int(tidspunkt[0])>=9 and int(tidspunkt[0])<=13:
            if int(dagen) == dayInMonth:
                resultat = f'high tide at {splitt[1]}'
    print (resultat)
checkTides(18)

def listTides():
    lavvann_sek, høyvann = genTides()
    lavvann = genTidesStr(lavvann_sek)
    dict_lavvann = {}
    for tidspunkt in lavvann:
        tidspunkt_lst = tidspunkt.split()
        dato = int(tidspunkt_lst[0])
        tid = tidspunkt_lst[1]
        try:
            dict_lavvann[dato].append(tid)
        except:
            dict_lavvann[dato] = [tid]
    print('Day', 'First'.ljust(9), 'Second')
    
    for key,val in dict_lavvann.items():
        if len(val)==2:
            print(str(key).rjust(3), val[0].ljust(9) , val[1])
        elif len(val)==1:
            print(str(key).rjust(3), val[0])

listTides()

1,13