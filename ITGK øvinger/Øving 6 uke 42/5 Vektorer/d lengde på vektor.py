import math
def vec_len(vektor):
    summen = 0
    for i in range (len(vektor)):
        summen += (vektor [i])**2
    return math.sqrt(summen)

vec1 = [1, 4, 3]
print(vec_len(vec1))