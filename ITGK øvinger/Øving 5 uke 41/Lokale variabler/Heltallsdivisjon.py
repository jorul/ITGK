def heltall(x,y):
    num = x//y
    return num
def kvadrat(x):
    num = x**2
    return num
tall1 = int(input('skriv et heltall: '))
tall2 = int(input('skriv et annet heltall: '))

print(f'Heltallsdivisjon av {tall1} over {tall2} gir {heltall(tall1,tall2)}')
print(f'Kvadratet av {tall1} er {kvadrat(tall1)}')