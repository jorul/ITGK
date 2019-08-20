def generate_license_numbers(amount):
    import random
    liste = []
    bokstaver = ['BS', 'CV', 'EL', 'FY', 'KU', 'LE', 'NB', 'PC', 'SY', 'WC']
    while len(liste)<amount:
        tall = str(random.randint(10000,100000))
        bilskilt = random.choice(bokstaver) + tall
        if bilskilt not in liste:
            liste.append(bilskilt)
    return liste

print(generate_license_numbers(7))
