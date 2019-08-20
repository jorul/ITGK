def insertion_sort(liste):
    for i in range(1,len(liste)):
        element= liste[i]
        hull = i
        while hull>0 and liste[hull-1]>element:
            liste[hull] = liste[hull-1]
            hull = hull-1
        liste[hull] = element
    return liste

A = ['Petter','Alex','Diana','Bodil','Anne']
print(insertion_sort(A))