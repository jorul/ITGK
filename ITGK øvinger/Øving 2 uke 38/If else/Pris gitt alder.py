alder = int(input('Din alder: '))
if alder>= 60:
    print('Bilettpris: 40kr')
elif alder >= 26:
    print('Bilettpris: 80kr')
elif alder >= 12:
    print('Bilettpris: 50kr')
elif alder >= 3:
    print('Bilettpris: 30kr')
else:
    print('Biletten er gratis')