def vector_dot_product(vektor1,vektor2):
    if len(vektor1) != len(vektor2):
        print ('Vektorene du ga meg har ikke samme lengde, da er min oppgave umulig, din fjompenisse.')
    summen = 0
    for i in range (len(vektor1)):
        summen += vektor1 [i] * vektor2[i]
    return summen
vec1 = [1, 4, 3]
vec2 = [2, 3.1, 5]
print("Prikkproduktet av",vec1,"og",vec2,"er:",format(vector_dot_product(vec1,vec2),".3f"))