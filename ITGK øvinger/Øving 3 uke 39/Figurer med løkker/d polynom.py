from turtle import*
print('Jeg kan tegne et regulært polygonet.')
kanter = int(input('Velg antall kanter: '))
omkrets = int(input('Velg omkrets på polygonet: '))
vinkel = (360/kanter)
lengde = (omkrets/kanter)
for i in range(kanter):
    forward(lengde)
    left(vinkel)
time.sleep(30)