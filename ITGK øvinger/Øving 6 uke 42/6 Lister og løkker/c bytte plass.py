number_list = []
for i in range(100):
    number_list.append(i)

byttetliste = []
for i in range (len(number_list)):
    if i%2 == 0:
        s = i+1
    else:
        s = i-1
    byttetliste.append(s)
print(byttetliste)