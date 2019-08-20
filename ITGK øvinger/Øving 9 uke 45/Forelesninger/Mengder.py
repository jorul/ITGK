A = set([1,2,3]) #skriv inn liste eller streng - deles opp til ulike elementer i mengden (hver bokstav i strengen)
A.add(8)

B = {1,2,3}
B.remove(2)

print(A) # gir {8,1,2,3}
print(B) # gir {1,3}

A.union(B) #Bare verdiene i begge
A.intersection(B) #Verdien i begge og den ene
A.difference(B) #Verdiene i kun A
A.symmetric_difference(B) #Verdiene i kun en av de

#DELSETT
A.issubset(B) #A er delmengde i B (gir False)
A.issuperset(B) #B er delmengde i A (gir True)

#PROTIP: konvertere mellom datatyper, eks. lister, dictionaries 