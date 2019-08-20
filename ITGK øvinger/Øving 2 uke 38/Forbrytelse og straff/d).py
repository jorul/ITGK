# leser inn data
prom = float(input("Hvor stor var promillen? "))
nekt = input("Nektet å samarbeide ved legetest? (j/n) ")
tidl = input("Tidligere dømt for promillekjøring? (j/n) ")
if tidl == "j":
    aar = int(input("Antall år siden siste domfellelse: "))
else:
    aar = 999
  
# vurderer inndragning av førerkort
if prom > 0.2 and (tidl == "j" or (nekt == "j" and aar < 5)):
    print("Førerkort inndras for alltid.")
elif prom > 1.2 or nekt == "j":
    print("Førerkort inndras minst 2 år.")
elif prom > 0.8:
    print("Førerkort inndras 20-22 mnd.")
elif prom > 0.5:
    print("Førerkort inndras vanligvis 18 mnd.")
elif prom > 0.2:
    print("Førerkort inndras inntil 1 år.")
else:
    print("Ingen inndragning av førerkort.")