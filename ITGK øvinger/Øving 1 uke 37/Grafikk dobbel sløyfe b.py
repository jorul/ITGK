from turtle import *
import time
# importerer funksjoner fra biblioteket turtle
pensize(8)      # setter penntykkelsen til 8
begin_fill()    # gjør at det som tegnes etter denne blir fyllt
circle(50)      # sirkel tegnes MOT klokka med radius 50
circle(-50)     # negativ radius: tegner MED klokka
end_fill()      # avslutter fyllingen
color("red")    # setter tegnefargen til rød
circle(70)
circle(-70)
time.sleep(10)  # Gjør at vinduet med tegningen ikke lukkes med én gang, men er oppe i 10 sekunder
