tid = int(input("Hvor mange minutt har kaken stått i ovnen? "))
if tid>= 50:
    print("Kaken kan tas ut av ovnen.")
    print("Tips til servering: vaniljeis.")
else:
    igjen = 50-tid
    print(f'Kaken skal stå i ovnen i minst {igjen} minutter til.')