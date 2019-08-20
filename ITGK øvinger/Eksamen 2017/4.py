def formatTime(seconds):
    hh = stringifikator(seconds//3600)
    tt = stringifikator((seconds%3600)//60)
    ss = stringifikator((seconds%3600)%60)
    return hh + ':' + tt + ':' + ss

def stringifikator(i):
    if i <10:
        return '0' + str(i)
    else:
        return str(i)

def valuesDecember():
    first = 3*60*60 + 18*60
    period = 12*60*60 + 25*60 +12
    return first, period

def genTides():
    first, period = valuesDecember()
    lavvannliste = []
    lavvann = first
    while lavvann <= 2764800: #2678400 sekunder i Desember
        lavvannliste.append(lavvann)
        lavvann += period
    høyvann = first + period//2
    høyvannliste = []
    while høyvann <= 2764800:
        høyvannliste.append(høyvann)
        høyvann += period
    return lavvannliste, høyvannliste

lows,highs = genTides()

print(lows[:8])
print(highs[:8])

def genTidesStr(tideList):
    nylista = []
    for i in tideList:
        dato = str(i//(60*60*24)+1)
        tidspunkt = formatTime(i%(60*60*24))
        nylista.append(dato + ' ' + tidspunkt)
    return nylista

lowStrings = genTidesStr(lows)
for item in lowStrings:
    print(item)

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

checkTides(24)

def listTides():
    print('Day  First    Second')
    lows,highs = genTides()
    mydict = {}
    for i in lows:
        dato = i//(60*60*24)
        tidspunkt = formatTime(i%(60*60*24))
        if dato in mydict:
            mydict[dato].append(tidspunkt)
        else:
            mydict[dato] =[tidspunkt]
    for dato in mydict.keys():
        if len(mydict[dato])==1:
            if len(str(dato))==1:
                print(f'  {dato+1} {mydict[dato][0]}')
            else:
                print(f' {dato+1} {mydict[dato][0]}')
        else:
            if dato <8:
                print(f'  {dato+1} {mydict[dato][0]} {mydict[dato][1]}')
            else:
                print(f' {dato+1} {mydict[dato][0]} {mydict[dato][1]}')

listTides()

        

