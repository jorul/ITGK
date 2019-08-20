dag = int(input('Dager til du skal reise? '))
stud = str.lower(input('Er du student? '))
if dag >= 14:
    if stud == 'ja':
        print(f'Som student får du minipris {199*0.9},- kan ikke refunderes/endres')
    else:
        print('Minipris 199,- kan ikke refunderes/endres')
    ønske = str.lower(input('Ønskes dette? '))
else:
    ingenting = 2
if dag<14 or ønske == 'nei':
    mill = str.lower(input('Er du i millitæret? '))
    alder = int(input('hvor gammel er du? '))
    if stud == 'ja':
        if alder>=60 or mill == 'ja':
            print(f'Prisen på din bilett blir: {440*0.75*0.75},-')
        if alder <16:
            print(f'Prisen på din bilett blir: {440*0.5*0.75}')
    elif alder>= 60:
        print(f'Prisen på din bilett blir: {440*0.75}')
    elif alder <16:
        print(f'Prisen på din bilett blir: {440*0.5}')
    else:
        print('Prisen på din bilett blir: 440')
print('Takk for pengene, god reise!')
