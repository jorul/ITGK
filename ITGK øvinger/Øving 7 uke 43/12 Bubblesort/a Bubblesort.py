def bubbleSort(liste):
    for y in range(len(liste)):
        for i in range(len(liste)-1):
            if liste[i]>liste[i+1]:
                iern = liste[i]
                iernpluss = liste[i+1]
                liste[i] = iernpluss
                liste[i+1] = iern
            
    return liste

liste = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]
print(bubbleSort(liste))