def seq(lst):
    for el in range(1,len(lst)):
        element = lst[el]
        hull = el
        while element<lst[hull-1]:
            lst[hull] =  lst[hull-1]
            hull -=1
        lst[hull] = element
    return lst

s= seq([1,4,7,9,2,3,5,6,8,])
print(s)

def binary(liste,element):
    mid = len(liste)//2
    if len(liste)<1:
        return False
    elif liste[mid]==element:
        return True
    elif element < liste[mid]:
        return binary(liste[0:mid], element)
    elif element >liste[mid]:
        return binary(liste[mid+1:len(liste)], element)

print(binary(s,9))
