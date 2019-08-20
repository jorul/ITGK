ukedagene = ['man', 'tir', 'ons', 'tor', 'fre', 'lør', 'søn']
def is_leap_year ( year ):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def weekday_newyear(året):
     if året == 1900:
        return 0
     else:
        ukedag = weekday_newyear(året-1) + 1
        if is_leap_year(året-1) == True:
            ukedag +=1
        svar = ukedag%7
        return svar

def is_workday(day):
    if 0 <= day <= 4:
        return True
    else:
        return False

def workdays_in_year(år):
    antall_arbeidsdager = 0
    første_dag = weekday_newyear(år)
    if is_leap_year(år) == True:
        antall_dager = 366
    else:
        antall_dager = 365
    for i in range(første_dag, antall_dager + første_dag):
        dagen = i%7
        if is_workday(dagen) == True:
            antall_arbeidsdager +=1
    return antall_arbeidsdager
for i in range(1900,1920):
    print(f'{i} har {workdays_in_year(i)} arbeidsdager')