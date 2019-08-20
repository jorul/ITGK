def summerOlympics(firstYear, lastYear):
    years = []
    første_OL = -1
    for s in range(firstYear,lastYear +1):
        if s %4 == 0:
            første_OL = s
    for i in range(s,lastYear+1,4):
        years.append(i)
    return years

def findAge(bYear,bMonth, bDay):
    yyyy,mm,dd = current_date()
    år = yyyy - bYear
    måned = mm - bMonth
    dag = dd - bDay
    if dag<0:
        måned -= 1
    if måned <0:
        år -= 1
    return år

def printAgeDiff(table):
    for p in range(len(table)-1):
        p_alder = findAge(table[p][2], table[p][3], table[p][4])
        neste_p_alder = findAge(table[p+1][2], table[p+1][3], table[p+1][4])
        if p_alder == neste_p_alder:
            print(f'{table[p][0]} {table[p][1]} is at the same age as {table[p+1][0]} {table[p+1][1]}')
        elif p_alder < neste_p_alder:
            print(f'{table[p][0]} {table[p][1]} is younger than {table[p+1][0]} {table[p+1][1]}')
        elif p_alder > neste_p_alder:
            print(f'{table[p][0]} {table[p][1]} is older than {table[p+1][0]} {table[p+1][1]}')

table=[['Justin','Bieber',1994,3,1],
['Donald','Duck',1934,8,1],
['George','Clooney',1961,5,6],
['Eddie','Murphy',1961,4,3]]
printAgeDiff(table)
    
