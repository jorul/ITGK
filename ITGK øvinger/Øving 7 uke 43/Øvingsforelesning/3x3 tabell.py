tabell_3x3 = [[0 for i in range (3)] for j in range(3)]

for i in range(3):
    for j in range(3):
        tabell_3x3[i][j] = i*6+j*2+2

for i in range (3):
    print(tabell_3x3[i])