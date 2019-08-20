
def imp2cm(fot,tomme):
    tommer = 12*fot + tomme
    cm = tommer*2.54
    return round(cm)

fot = int(input("Oppgi antall fot: "))
tommer = int(input("Oppgi antall tommer: "))
cm = imp2cm(fot, tommer)
print("Det blir", cm, "cm")
