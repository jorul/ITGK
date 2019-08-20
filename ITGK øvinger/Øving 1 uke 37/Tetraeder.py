h = input('Skriv inn høyde: ')

from math import*
a = (3/sqrt(6))*float(h)
Ar = sqrt(3)*(float(a))**2
V = (sqrt(2)*(float(a))**3)/12

print('Et tetraeder med høyde', h,'har volum', round(float(V),2), ' og areal', round(float(Ar),2))
