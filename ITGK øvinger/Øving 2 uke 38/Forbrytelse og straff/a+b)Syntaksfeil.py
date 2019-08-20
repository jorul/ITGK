# leser inn data
prom = float(input("Hvor stor var promillen? "))
motor = input("Var farkosten en motorvogn? (j/n) ")
f = input("Var personen fører av vognen? (j/n) ")
leds = input("Var personen ledsager ved øvekjøring? (j/n) ")
n = input("Var det nødrett? (j/n) ")
 
# vurderer straffbarhet
if prom > 0.2 and motor == "j" and (f == "j" or leds == "j") and n == "n":
   print("Det var straffbar promillekjøring.")
else:
    print("Ikke straffbart, ingen bot.")