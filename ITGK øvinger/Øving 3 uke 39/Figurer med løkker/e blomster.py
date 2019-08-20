from turtle import*
print('Jeg kan tegne en blomst av regulære polygonet.')
kanter = int(input('Velg antall kanter i polygonet: '))
omkrets = int(input('Velg omkrets på polygonet: '))
antall = int(input(f'Velg antall {kanter}-kanter i blomsten: '))
vinkel = (360/kanter)
lengde = (omkrets/kanter)
bg = input('Ønsket bakgrunnsfarge: ')
bgcolor(bg)
pensize(2)
for x in range(antall):
    pen = input(f'farge på {kanter}-kant nummer {x+1}: ')
    color(pen)
    for i in range(kanter):
        forward(lengde)
        left(vinkel)
    left(360/antall)