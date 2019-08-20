import math
def edgeLength(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def circumference(pList):
    if len(pList)== 0 or len(pList)%2 != 0:
        return-1
    elif len(pList)==2:
        return 0
    elif len(pList)==4:
        return 2*edgeLength(pList[0],pList[1],pList[2],pList[3])
    else:
        omkrets = 0
        for i in range(2,len(pList),2):
            lengde = edgeLength(pList[i-2], pList[i-1],pList[i],pList[i+1])
            omkrets += lengde
        lengde = edgeLength(pList[0], pList[1],pList[len(pList)-2],pList[len(pList)-1]) #Den siste kanten
        omkrets += lengde 
        return omkrets

print(circumference([3, 1, 5, 4, 4, 5, 2, 4, 1, 2]))

def enclosingRectangle(pList):
    lavest_x = pList[0]
    høyest_x = pList[0]
    lavest_y = pList[1]
    høyest_y = pList[1]
    for x in range(0,len(pList),2):
        if pList[x]>høyest_x:
            høyest_x = pList[x]
        if pList[x]<lavest_x:
            lavest_x = pList[x]
    for y in range(1, len(pList),2):
        if pList[y]>høyest_y:
            høyest_y = pList[y]
        if pList[y]<lavest_y:
            lavest_y = pList[y]
    return [lavest_x, lavest_y, høyest_x, høyest_y]
print(enclosingRectangle( [3, 1, 5, 4, 4, 5, 2, 4, 1, 2]))

def readPolygonFile(filename):
    f = open(filename, 'r')
    listami = []
    for linje in f:
        linje_liste= linje.strip().split()
        listami.append(int(linje_liste[0]))
        listami.append(int(linje_liste[1]))
    f.close()
    return listami
