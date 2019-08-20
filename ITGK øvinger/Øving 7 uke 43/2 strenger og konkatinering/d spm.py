def func1(liste):
    streng = ""
    for s in liste:
        if len(s)>3:
            streng += s[3]
    return streng
  
def func2(streng):
    streng += streng
    return streng
  
print(func2(func1(["Klabert","Oslo","Tur","stubbe"])))

#vil skrive ut bobbob