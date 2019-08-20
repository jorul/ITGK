def rank_stores(storeList, sumStores):
    for i in range(len(sumStores)):
        butikk = storeList[i]
        pris = sumStores[i]
        index_hull = i
        while index_hull>0 and pris<sumStores[index_hull-1]:
            sumStores[index_hull]= sumStores[index_hull-1]
            storeList[index_hull]= storeList[index_hull-1]
            index_hull -=1
        storeList[index_hull] = butikk
        sumStores[index_hull] = pris
    return storeList

print(rank_stores(['J', 'T', 'I','S', 'M', 'A'], [0,10,5,7,4,6]))

def adjust_string(text, length):
    if len(text)==30:
        return text
    if len(text) >30:
        return text[:31]
    vs = int((30-len(text))//2)
    hs = int(vs + (30-len(text))%2) #dersom det er oddetall antall mellomrom som skal til for at det blir 30
    ny_tekst = ' '*vs + text + ' '*hs
    return ny_tekst

print(adjust_string('hei',30))

import time
def display_from_file(filename):
    f = open(filename,'r')
    komplettliste = []
    for line in f:
        line = line.strip()
        line30 = adjust_string(line,30)
        komplettliste.append(line30)
    #Nå er komplettliste ei liste med alle linjene i filen lagret med riktig lengde
    
    antall = len(komplettliste)//6 #antall ganger noe nytt skal vises
    for i in range(antall):
        liste_nå = komplettliste[i*6:i*6+6]
        show_display(liste_nå)
        time.sleep(10)