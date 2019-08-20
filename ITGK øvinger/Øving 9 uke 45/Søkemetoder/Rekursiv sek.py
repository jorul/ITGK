def recursive(liste, element):
    print(liste)
    if len(liste)==0:
        return False
    if liste[0] == element:
        return True
    return recursive(liste[1:], element)

print(recursive([1,2,3,4,5,6],4))