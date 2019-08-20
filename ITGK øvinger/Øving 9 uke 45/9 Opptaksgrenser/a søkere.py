
def linjer_med_alle(filename):
    teller = 0
    file = open(filename, 'r')
    for line in file:
        splittet = line.split(',')
        kom_inn = splittet[1].rstrip('\n')
        if kom_inn == '"Alle"':
            teller +=1
    file.close()
    return teller

print(linjer_med_alle('poenggrenser_2011.txt'))