def reversed_word(str):
    ordet =''
    for i in range(len(str)-1,-1,-1):
        ordet += str[i]
    return ordet

string = 'star desserts'
print(reversed_word(string))