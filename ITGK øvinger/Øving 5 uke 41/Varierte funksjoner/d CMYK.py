def cmyk2rgb(C,M,Y,K):
    R = 255 * (1-C) * (1-K)
    G = 255 * (1-M) * (1-K)
    B = 255 * (1-Y) * (1-K)
    return R, G, B
  
  
print("Oppgi farge i CMYK og få det konvertert til RGB.")
C = float(input("C: "))
M = float(input("M: "))
Y = float(input("Y: "))
K = float(input("K: "))
R, G, B = cmyk2rgb(C, M, Y, K)
print("Som RGB:", R, G, B)
  
# viser fargen på skjermen:
from turtle import colormode, bgcolor
colormode(255)
bgcolor(int(R), int(G), int(B))