n = int((input('n = ')))
tall = 0
t=0
for i in range (1, n+1):
    rest = i%2
    if rest == 0:
        t = -i**2
    else:
        t = i**2
    tall = tall + t
print(tall)