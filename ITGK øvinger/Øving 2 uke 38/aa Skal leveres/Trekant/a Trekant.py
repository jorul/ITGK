import time
from turtle import *
# importerer funksjoner fra turtle
print("Hei, jeg kan tegne en trekant")

penn = str.upper(input('Velg pennefarge, NTNU-rosa (R) eller NTNU-turkis (T):'))
fyll = str.upper(input('Fyllfarge, NTNU-gul (G), -oransj (O), -lilla (L): '))
retning = str.lower(input('Ønsker du spissen på trekanten opp eller ned? '))
pensize(7)          # sett pennen 7 piksler tykk
if penn == 'R':
    pencolor("#ad208e")
if penn == 'T':
    pencolor("#5cbec9")

if fyll == 'G':
    fillcolor("#d5d10e")
if fyll == 'O':
    fillcolor('#f58025')
if fyll == 'L':
    fillcolor('#552988')
bgcolor("#00509e") # sett fyllfargen lilla
# Tegner en fylt trekant
begin_fill()
if retning == 'ned':
    left(180)
forward(200)        # gå 100 piksler framover
left(120)           # drei 120 grader venstre
forward(200)  
left(120) 
forward(200)
end_fill()
  
# Holder vinduet med tegningen åpent i 10 sekunder. Ha dette som siste linje i koden din
time.sleep(10)