from turtle import *
import time
 
# setter opp tegnevinduet
setup(330, 330, 0, 0)
screensize(315, 315)
goto(-60, 150)

bg = input('Hvilken farge skal bakgrunnen ha? ')
fk = input('Hvilken farge skal firkanten ha? ')
 
# velger farger
bgcolor(bg)
color(fk)
 
#tegner den indre firkanten
begin_fill()
right(10) # tilter den 10 grader nedover
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
end_fill()
  
time.sleep(10)      # Gjør at vinduet med tegningen ikke lukkes med én gang, men er oppe i 10 sekunder
