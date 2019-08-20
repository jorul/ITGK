a = float(input('Skriv inn et desimaltall: '))
d = float(input('Antall desimaler i avrunding: '))

import math
des = (float((a*10**d)-(math.floor(a*10**d))))
if des<(0.5):
    print(math.floor(a*10**d)/10**d)
else:
    print(math.ceil(a*10**d)/10**d)
