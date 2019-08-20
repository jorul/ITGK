def multiplication_table(n):
    gangetabell = []
    for i in range (1,n+1):
        en_linje = []
        for p in range (1,n+1):
            en_linje.append(i*p)
        gangetabell.append(en_linje)
    return gangetabell

#print(multiplication_table(10))
tabellen = multiplication_table(4)
for i in range (len(tabellen)):
    print(tabellen[i])
