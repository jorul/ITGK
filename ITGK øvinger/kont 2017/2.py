def file_to_list(filename):
    nyliste = []
    f = open('filename', 'r')
    for linje in f:
        liste = linje.strip().split()
        liste[2] = float(liste[2])
        nyliste.append(liste)
    return nyliste

def list_stores(dataList):
    butikker = []
    for i in datalist:
        if i[0] not in butikker:
            butikker.append(i[0])
    return butikker #storeList

def sum_prices_stores(dataList,storeList):
    priser = []
    for butikk in storeList:
        sumbutikk = 0
        for varer in dataList:
            if butikk == varer[0]:
                sumbutikk += varer[2]
        priser.append(sumbutikk)
    return priser #sumStores

def rank_stores(storeList, sumStores):
    rangert = []
    kobling = {}
    for i in range(len(storeList)):
        kobling[sumStores[i]] = storeList[i]
    sumStores.sort()
    for j in sumStores:
        rangert.append(kobling[j])
    return rangert

        
def store_analysis(filename):
    liste = file_to_list(filename)
    butikker = list_stores(liste)
    priser = sum_prices_stores(liste,butikker)
    rangering = rank_stores(butikker, priser)
    print('The total price for shopping per store is:')
    for i in range(len(butikker)):
        print(f'{butikker[i]} : {priser[i]} kr')
    print('')
    print('The ranking of stores according to prices is:')
    for i in range(len(butikker)):
        print(f'{i+1} {rangert[i]}')

