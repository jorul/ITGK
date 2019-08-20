def inputPerson():
    navn = input('Name: ')
    Id = input('ID: ')
    vekt = int(input('KG: '))
    size = int(input('Size: '))
    return [navn, Id, vekt, size]

def readDbFile(filename):
    f = open(filename,'r')
    liste = []
    for line in f:
        line = line.strip()
        line_list = line.split(';')
        line_list[2] = int(line_list[2])
        line_list[3] = int(line_list[3])
        liste.append(line_list)
    f.close()
    return liste

def printMemberList(db):
    print('NAMN'.ljust(15), 'ID-NR'.ljust(9), 'VEKT'.rjust(5), 'kg.', 'SKJERMSTORLEIK')
    for i in range(len(db)):
        print((db[i][0]).ljust(15), (db[i][1]).ljust(9), str((db[i][2])).rjust(5), 'kg', str((db[i][3])).ljust(4), 'kvadratfot')

db=[['Frank Stank', 'D-49334', 75, 120], ['Bjarne Stor', 'C-49335', 95, 150], ['Dumbo Ear', 'D-50105', 450, 750], ['Peter Pan', 'A-12345', 30, 100]]
printMemberList(db)

def addperson(filename):
    person = inputPerson()
    f = open(filename, 'a')
    streng = f'{person[0]};{person[1]};{person[2]}'
    f.write(streng)
    f.close()
    db = readDbFile(filename)
    return db

def feet2seconds(feet):
    if feet <= 3000:
        return 0
    if feet <= 4000:
        return (feet-3000)/100
    return (feet-4000)/200 + 10


