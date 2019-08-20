print("Gi inn a og b, begge heltall i intervall <40,50> eller <70,90>:" )
a = int(input("Verdi for a: "))
b = int(input("Verdi for b: "))
  
if (70<a<90 or 40<a<50) and (70<b<90 or 40<b<50):
    print("Tallene er begge i gyldige intervall ^u^")
else:
    print("Minst ett av tallene er utenfor et gyldig intervall :(")