def selection_sort(liste):
    nyliste = []
    while liste != []:
        størstindex = 0
        for i in range(len(liste)):
            if liste[i] > liste[størstindex]:
                størstindex = i
        nyliste.append(liste.pop(størstindex))
    nyliste.reverse()
    return nyliste

liste = [9,1,34,7,2,3,45,6,78,56,36,65,33,21,23,34,45,6]
print(selection_sort(liste))