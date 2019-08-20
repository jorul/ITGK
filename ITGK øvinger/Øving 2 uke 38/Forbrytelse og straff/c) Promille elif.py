prom = float(input("Hvor stor var promillen? "))
if prom < 0.2:
    print("Ikke straffbart, ingen bot.")
elif prom <= 0.4:
    print("Forelegg: 6000,-")
elif prom <= 0.5:
    print("Forelegg: 10000,-")
else:
    print("Bot: en halv brutto månedslønn, samt fengsel.")


def promille(x):
    if x < 0.2:
        print("Ikke straffbart, ingen bot.")
    elif x <= 0.4:
        print("Forelegg: 6000,-")
    elif x <= 0.5:
        print("Forelegg: 10000,-")
    else:
        print("Bot: en halv brutto månedslønn, samt fengsel.")
promille(prom)