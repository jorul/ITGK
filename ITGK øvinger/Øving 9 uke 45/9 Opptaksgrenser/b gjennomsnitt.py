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

def gjennomsnitt_NTNU(filename):
    summen = 0
    antall_linjer = 0
    file = open(filename, 'r')
    for line in file:
        studie = line[1:5]
        if studie == 'NTNU':
            splittet = line.split(',')
            grense = splittet[1].rstrip('\n')
            if grense != '"Alle"':
                summen += float(grense)
                antall_linjer += 1
    file.close()
    return summen/antall_linjer

print(gjennomsnitt_NTNU('poenggrenser_2011.txt'))

def laveste_opptaksgrense(filename):
    linjenavn = ''
    grense = 65
    file = open(filename, 'r')
    for line in file:
        splittet = line.split(',')
        current_grense = splittet[1].rstrip('\n')
        if current_grense != '"Alle"'and float(current_grense) <grense:
            grense = float(current_grense)
            linjenavn = splittet[0]
    file.close()
    return linjenavn

print(laveste_opptaksgrense('poenggrenser_2011.txt'))

def dictionary(filename):
    diction = {}
    file = open(filename, 'r')
    for line in file:
        uten = line.replace('"',' ')
        ordrett = uten.split()
        skole = ordrett[0]
        linje= ordrett[2]
        grense = ordrett[len(ordrett)-1]
        try:
            diction[skole].append({linje:grense})
        except:
            diction[skole] = [{linje:grense}]
    return diction


print(dictionary('poenggrenser_2011.txt'))