i = 42
while i > 0:
    print(f'Du har nå {i} bokstaver til disposisjon')
    adj = input("Beskriv deg selv med et adjektiv? ")
    if len(adj) > i:
        print('Hvis du bare skal være en juksepave så får du ikke bruke dette programmet lengre.')
        break
    print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
    i = i- len(adj)
print("Takk for nå!")