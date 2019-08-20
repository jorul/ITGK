def weatherStats(weatherData):
    antall_dager = len(weatherData)
    high_temp_day = 0
    low_temp_day = 0
    total_rain = weatherData[0][2]
    for i in range(1,antall_dager):
        if weatherData[i][0]> weatherData[high_temp_day][0]:
            high_temp_day = i
        if weatherData[i][1]>weatherData[low_temp_day][1]:
            low_temp_day = i
        total_rain += weatherData[i][2]
    print(f'There are {antall_dager} days in the period.')
    print(f'The highest temperature was {weatherData[high_temp_day][0]} C on day number {high_temp_day}')
    print(f'The lowest temperature was {weatherData[low_temp_day][1]} C on day number {low_temp_day}')
    print(f'There was a total of {total_rain} mm rain in the period.')

def coldestThreeDays(weatherData):
    dict_three_days = {}
    for i in range(len(weatherData)-2): #lagrer verdiene for hver 'tredager'
        dict_three_days[i]= (weatherData[i][1] + weatherData[i+1][1]+weatherData[i+2][1])/3
    coldest_three_days = 0
    for keys in dict_three_days.keys():
        if dict_three_days[i] <= dict_three_days[coldest_three_days]: #sammenligner, returnerer den siste hvis lik
            coldest_three_days = keys
    return coldest_three_days+1 #+1 fordi 0 = dag 1 osv

def addNewDay(extraData, weatherStats):
    liste_ed = extraData.split(', ')
    liste_ed[0] = float(liste_ed[0].strip('max='))
    liste_ed[1] = float(liste_ed[1].strip('min='))
    liste_ed[2] = float(liste_ed[2].strip('mm'))
    weatherStats.append(liste_ed)
    return weatherStats


weatherData = [[12.0, 2.4, 8.2], [6.1, 0.6, 11.9], [8.3, -3.5, 0.0], [11.6, -5.2, 0.0], [15.3, 2.8, 14.3]]
weatherStats(weatherData)
print(coldestThreeDays(weatherData))
extraData = 'max=23.5, min=9.3, 5.1mm'
print(addNewDay('max=23.5, min=9.3, 5.1mm',weatherData))
