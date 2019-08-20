print('Slå Enter uten å skrive noe når du vil avslutte.')
adj = input("Beskriv deg selv med et adjektiv? ")
while adj != '':
    print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
    adj = input("Beskriv deg selv med et adjektiv? ")
print("Takk for nå!")