import time
from turtle import *
 
pensize(2)              #setter pennen 2 piksler tykk
pencolor("purple")      #setter pennefargen til lilla
bgcolor("yellow")       #setter bakgrunnsfargen til gul
hideturtle()            #skjuler pila
 
def halfPetal():        #lager et halvt blomsterblad
    forward(50)
    left(30)
    forward(75)
    left(30)
    forward(50)
    left(120)
 
def petal():            #lager et helt blomsterblad
    for i in range(2):
        halfPetal()
  
  
# Holder vinduet med tegningen åpent i 10 sekunder. Ha dette som siste linje i koden din
time.sleep(10)