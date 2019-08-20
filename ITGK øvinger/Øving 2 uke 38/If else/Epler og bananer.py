epler = int(input("Hvor mange epler har du? "))
barn = int(input("Hvor mange barn passer du? "))
if barn >0:
    prbarn = epler//barn
    tildeg = epler%barn
    if prbarn == 1:
        print("Da blir det", prbarn, "eple til hvert barn")
    else:
        print("Da blir det", prbarn, "epler til hvert barn")
    if tildeg == 1:
        print("og", tildeg, "eple til overs til deg selv.")
    else:
       print("og", tildeg, "epler til overs til deg selv.")

print("Takk for i dag!")