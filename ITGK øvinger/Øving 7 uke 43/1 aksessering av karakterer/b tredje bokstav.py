def en_bokstav(dittord, nummer):
    if nummer > len(dittord):
        return q
    else:
        return dittord [nummer-1]

ordet = input('Skriv inn et ord: ')
nr = int(input('Hvilken bokstav vil du ha? '))

print(en_bokstav(ordet, nr))
