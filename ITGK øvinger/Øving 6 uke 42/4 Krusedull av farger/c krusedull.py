import math
import turtle
oddetall = []
for i in range(1,20,2):
    oddetall.append(i)

brukerfarger = (input('Skriv 10 farger med komma og mellomrom mellom: '))
farger = brukerfarger.split (', ')
wn = turtle.Screen()
for i in range (len(oddetall)):
    turtle.setposition(0,0)
    turtle.pencolor(farger[i])
    for p in range(41):
        turtle.forward(oddetall[i]*len(oddetall))
        turtle.left(123)
