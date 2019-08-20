teeth = [95,103,71,99,114,64,95,53,97,114,109,11,2,21,45,2,26,81,54,14,118,108,117,27,115,43,70,58,107]
mynter = []
for i in range (len (teeth)):
    mynter_for_tann = []
    kroner = teeth[i]
    mynter_for_tann.append(kroner //20)
    kroner = kroner%20
    mynter_for_tann.append(kroner //10)
    kroner = kroner%10
    mynter_for_tann.append(kroner //5)
    kroner = kroner%5
    mynter_for_tann.append(kroner)
    mynter.append(mynter_for_tann)
print(mynter)


for i in range(len(teeth)):
    print(mynter[i])