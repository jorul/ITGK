def skalarmultiplikasjon(liste, skalar):
    for i in range (len(liste)):
        liste [i] = liste [i]*skalar
    return liste
print(skalarmultiplikasjon([1.2, 4.5, 4.4],4))