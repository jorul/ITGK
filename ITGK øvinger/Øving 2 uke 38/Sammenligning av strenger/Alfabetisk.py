navn1 = input('Første navn: ')
navn2 = input('Andre navn: ')
print('Under følger navnene i alfabetisk rekkefølge:')
if navn1<navn2:
    print(navn1)
    print(navn2)
elif navn1>navn2:
    print(navn2)
    print(navn1)
else:
    print('Navnene er like')