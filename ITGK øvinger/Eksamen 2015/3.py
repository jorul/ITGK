def readTime():
    timer = []
    for i in range(23):
        timer.append(i)
    minutter = []
    for i in range(60):
        minutt.append(i)

    time = int(input('Enter hour: '))
    while time not in timer:
        print('- ERROR: Hour must be between 0 and 23!')
        time = int(input('Enterhour: '))
    
    minutt= int(input('Enter minute: '))
    while minutt not in minutter:
        print('- ERROR: Minute must be between 0 and 59!')
        minutt= int(input('Enter minute: '))
    
    sekund = int(input('Enter second: '))
    while sekund not in minutter:
        print('- ERROR: Second must be between 0 and 59!')
        sekund = int(input('Enter second: '))
    return [time, minutt, sekund]

def convertTime(time, mode):
    if mode == 'time':
        timer = time //3600
        minutt = (time%3600)//60
        sekund = (time%3600)%60
        return[timer,minutt,sekund]
    elif mode == 'sec':
        return time[0]*3600+time[1]*60 + time[2]

def travelTime():
    print('Give departure time in hour, minute and second: ')
    tid_start = readTime()
    sec_start = convertTime(tid_start, 'sec')

    print('Give arrival time in hour, minute and second: ')
    tid_slutt = readTime()
    sec_slutt = convertTime(tid_start, 'sec')
    tid_reise_i_sec = sec_slutt - sec_start
    while tid_reise_i_sec <0:
        print('-ERROR: Arrival time must be later than Departure time')
        tid_slutt = readTime()
        sec_slutt = convertTime(tid_start, 'sec')
        tid_reise_i_sec = sec_slutt - sec_start
    tid_reise_tabell = convertTime(tid_reise_i_sec, 'time')
    print(f'Traveltime: {tid_reise_tabell[0]} hours, {tid_reise_tabell[1]} min, {tid_reise_tabell[2]} sec')

def analyzeBusRoutes(BusTables):
    fastest_index = 0
    slowest_index = 0
    for i in range(len(BusTables)):
        bus_i_tid = (BusTables[i][3]-BusTables[i][1])*60 + BusTables[i][4]-BusTables[i][2]
        bus_fastest_tid = (BusTables[fastest_index][3]-BusTables[fastest_index][1])*60 + BusTables[fastest_index][4]-BusTables[fastest_index][2]
        bus_slowest_tid = (BusTables[slowest_index][3]-BusTables[slowest_index][1])*60 + BusTables[slowest_index][4]-BusTables[slowest_index][2]
        if bus_i_tid < bus_fastest_tid:
            fastest_index = i
        if bus_i_tid > bus_slowest_tid:
            slowest_index =i
    bus_slowest_tid = (BusTables[slowest_index][3]-BusTables[slowest_index][1])*60 + BusTables[slowest_index][4]-BusTables[slowest_index][2]
    bus_slowest_timer = bus_slowest_tid//60
    bus_slowest_min = bus_slowest_tid%60
    
    bus_fastest_tid = (BusTables[fastest_index][3]-BusTables[fastest_index][1])*60 + BusTables[fastest_index][4]-BusTables[fastest_index][2]
    bus_fastest_timer = bus_fastest_tid//60
    bus_fastest_min = bus_fastest_tid%60

    print(f'The slowest bus route is bus nr. {BusTables[slowest_index][0]} and it takes {bus_slowest_timer} hour, {bus_slowest_min} min.')
    print(f'The fastest bus route is bus nr. {BusTables[fastest_index][0]} and it takes {bus_fastest_timer} hour, {bus_fastest_min} min.')

Busses=[[1,15,0,15,19],[3,15,32,16,45],[4,15,45,16,23],[5,15,55,16,11]]
analyzeBusRoutes(Busses)