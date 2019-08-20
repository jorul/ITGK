def knop2km_t(x):
    knop = x*0.514444444*3.6
    return knop

knop = float(input("Oppgi fart i knop: "))
km_t = knop2km_t(knop)
print("Det blir", round(km_t, 2), "km/t")