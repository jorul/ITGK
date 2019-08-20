from turtle import *
from random import random,  randint
pensize(5)
R,G,B = random(), random(), random()
tilt = random() + 0.5
sides = randint(5,9)
for i in range(300):
    x = (300-i)/300
    color(R, G, B)
    forward(i)
    left(360/sides + tilt)
    R,G,B = 1-R, 1-G, 1-B