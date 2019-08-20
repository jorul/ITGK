from turtle import *
import time
 
# setter opp tegnevinduet
setup(330, 330, 0, 0)
screensize(315, 315)
goto(-60, 150)
# bruker angir tall for farger
bg = input('Gi et tall mellom 0 og 16777215 for ønsket bakgrunnsfarge ')
fk = input('Gi et tall mellom 0 og 16777215 for ønsket farge på ')

# finner ønskede farger
Rb = float(bg)//256**2
Gb = (float(bg)%256**2)//256
Bb = (float(bg)%256**2)%256

Rf = float(fk)//256**2
Gf = (float(fk)%256**2)//256
Bf = (float(fk)%256**2)%256

# velger farger
colormode(255)
bgcolor(int(Rb),int(Gb),int(Bb))
color(int(Rf),int(Gf),int(Bf))
 
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
  
time.sleep(15)      # Gjør at vinduet med tegningen ikke lukkes med én gang, men er oppe i 10 sekunder
