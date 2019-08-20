def addSite(notebook):
    site = input('What is he site: ')
    username = input('Write username: ')
    password = input('Write password: ')
    if site not in notebook.keys():
        notebook[site] = [username,[password]]
        print(f'Account added for {site}')
    return notebook

def showSites(notebook):
    print('Nettsted:'.ljust(17),'Brukernavn:'.ljust(15), 'Password:')
    for key in notebook.keys():
        site_name = key[0:16] + ':'
        print(site_name.ljust(17), notebook[key][0].ljust(15), notebook[key][1][-1]) #-1 gir siste element i lista

notebook = {'Facebook': ['Urgle',['pwd1']],
'reddit': ['urgle',['asdf1234','pwd1']],
'Aftenposten': ['ivrig',['pwdold','pwdnew']]}

def formatList(liste):
    streng = ''
    for element in liste:
        streng += str(element) + ', '
    streng = streng.strip(', ')
    return streng

def editSite(notebook, site):
    new_pass = input(f'Add new site password for {site}:')
    tidligere_passord = notebook[site][1]
    while new_pass in tidligere_passord:
        print(f'{new_pass} have been used for {site} already.')
        tidligere_passord_streng = formatList(tidligere_passord)
        print(f'The following passwords have been used for {site}: {tidligere_passord_streng}')
        new_pass = input(f'Add new site password for {site}:')
    notebook[site][1].append(new_pass)
    print(f'{site} has been updated with new password.')

def secureSites(notebook):
    problem_sites = []
    all_sites = []
    for keys in notebook.keys():
        all_sites.append(keys)
    for i in range(len(all_sites)):
        same_password = [all_sites[i]]
        for j in range(i+1,len(all_sites)):
            if notebook[all_sites[i]][1][-1] == notebook[all_sites[j]][1][-1]:
                same_password.append(all_sites[j])
        
        if len(same_password) > 1 and notebook[all_sites[i]][1][-1] != None: # antar at passord ikke kan være ingenting
            problem_sites.append(same_password)
            for element in same_password:
                notebook[element][1].append(None) #vil forhindre at det legges til flere ganger dersom mer enn to sider deler passord

    if len(problem_sites) == 0:
        print('No sites had similar passwords. Good job!')
    else:
        for liste in problem_sites:
            s = formatList(liste)
            print(f"You have used the password '{notebook[liste[0]][1][-2]}' on the following pages: {liste}")
            
            for site in liste:
                notebook[site][1] = notebook[site][1][:len(notebook[site][1])-2]



secureSites({'Facebook': ['Urgle',['oldpwd', 'pwd1']], 'reddit': ['Urgle',['pwd1']]})


def importResults(file):
    filnavn = file
    while filnavn != 'q':
        try:
            f = open(filnavn, 'r')
        except:
            filnavn = input(f"'{filnavn}' could not be found. File name('q' exits): ")
        if filnavn == 'q':
            return None
    listami = []
    for line in f:
        tekst = line.strip()
        listami.append(tekst)
    f.close()
    return listami

def analyzeResults(results):
    better_results = []
    for kamp in results:
        kampliste = kamp.split(',')
        kampliste.append(int(kampliste[2][2]))
        kampliste[2] = int(kampliste[2][0])
        better_results.append(kampliste)
    return better_results

def calculateScores(homeGoals, awayGoals):
    if homeGoals == awayGoals:
        return 1,1
    if homeGoals>awayGoals:
        return 3,0
    if awayGoals<homeGoals:
        return 0,3

def sumTeamValues(analyzed):
    lagoversikt = {}
    for kamp in analyzed:
        hjemmelag = kamp[0]
        bortelag = kamp[1]
        hjemmescore, bortescore = calculateScores(kamp[2],kamp[3])
        if hjemmelag not in lagoversikt.keys():
            lagoversikt[hjemmelag] = [hjemmescore, 1]
        else:
            lagoversikt[hjemmelag][0] += hjemmescore
            lagoversikt[hjemmelag][1] += 1
        
        if bortelag not in lagoversikt.keys():
            lagoversikt[bortelag] = [hjemmescore, 1]
        else:
            lagoversikt[bortelag][0] += bortescore
            lagoversikt[bortelag][1] += 1
    return lagoversikt

def showResults(analyzed):
    print('#############################################')
    for kamp in analyzed:
        home, away = calculateScores(kamp[2], kamp[3])
        if home == away:
            r = '(U)'
        elif home > away:
            r = '(H)'
        elif home < away:
            r = '(B)'
        print('# ', end = '')
        print(kamp[0].ljust(14), kamp[1].ljust(14), str(kamp[2]).rjust(2), '-' ,str(kamp[3]).rjust(2), r, '#' )
    print('#############################################')

showResults([['vinner','taper',6,2],['kult lag', 'teit lag',8,2]])

def most_points(team_data, teams):
    mest_poeng = teams[0]
    kamper_spilt = team_data[teams[0]][1]
    for lag in teams:
        if team_data[lag][0] > mest_poeng:
            mest_poeng = lag
            kamper_spilt = team_data[lag][1]
        elif team_data[lag][0] == mest_poeng:
            if kamper_spilt <team_data[lag][1]:
                mest_poeng = lag
                kamper_spilt = team_data[lag][1]
    return mest_poeng

def savePoints(team_data):
    teams = []
    for lag in team_data.keys():
        teams.append(lag)
    f = open('Points.txt', 'w')
    f.write('###################################')
    f.write('# Navn'.ljust(14), 'Poeng'.ljust(7), 'Kamper'.ljust(7), '#')
    for linje in range(len(teams)):
        lag_nå = most_points(team_data, teams)
        f.write('#', lag_nå.ljust(14), str(team_data[lag_nå][0]).ljust(7), str(team_data[lag_nå][1]).ljust(7), '#')
    f.write(('###################################'))



