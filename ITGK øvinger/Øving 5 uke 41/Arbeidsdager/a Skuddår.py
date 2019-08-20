def is_leap_year ( year ):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

ukedagene = ['man', 'tir', 'ons', 'tor', 'fre', 'lør', 'søn']

def weekday_newyear(året):
     if året == 1900:
        return 0
     else:
        ukedag = weekday_newyear(året-1) + 1
        if is_leap_year(året-1) == True:
            ukedag +=1
        svar = ukedag%7
        return svar 
for i in range (1900,1920):
    print(i, ukedagene[weekday_newyear(i)])   