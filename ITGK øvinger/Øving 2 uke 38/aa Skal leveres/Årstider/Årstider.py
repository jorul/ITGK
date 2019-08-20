M = str.lower(input('Måned: '))
D = int(input('Dag: '))
if D>31:
    print('Ingen måneder har mer enn 31 dager din fjott!')
elif M== 'desember' and D>=21 or M== 'januar' or M == 'februar' or M== 'mars' and D<20:
    print('Vinter')
elif M== 'mars' and D>=20 or M=='april' or M== 'mai' or M== 'juni' and D<21:
    print('Vår')
elif M== 'juni' and D>= 21 or M== 'juli' or M== 'august' or M== 'september' and D<22:
    print('Sommer')
elif M== 'september' and D>= 22 or M== 'oktober' or M== 'november' or M== 'desember' and D<21:
    print('Høst')
else:
    print(f'Ingen måneder heter {M} din fjott!')