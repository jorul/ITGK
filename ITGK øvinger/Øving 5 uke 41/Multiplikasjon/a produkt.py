def produkt(tol):
    endring = 1000
    count = 0
    prod =1
    prodny = 1
    while endring >= tol:
        count += 1
        prodny = prod * (1 + (1/(count**2)))
        endring = prodny-prod
        prod = prodny
    return [count, prodny]

toleranse = float(input('Angi toleransegrense: '))
svarliste = produkt(toleranse)
print (f'Produktet ble {round(svarliste[1],2)} etter {round(svarliste[0])} iterasjoner')