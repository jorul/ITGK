print(ord('a'))
print(chr(122))

def avstand_alfabet(bok1, bok2):
    return abs((ord(bok1)-ord(bok2)))

def avstand_ord(ord1, ord2):
    sum = 0
    min_lengde = min(len(ord1), len(ord2))
    for i in range (min_lengde):
        sum += (avstand_alfabet(ord1[i], ord2[i]))
    return sum

print(avstand_ord('a', 'ø'))
