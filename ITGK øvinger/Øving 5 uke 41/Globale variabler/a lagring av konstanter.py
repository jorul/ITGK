from math import sqrt
GRAVITY = 9.81
def get_fall_time(x):
    t = sqrt(2*x/GRAVITY)
    return t

meter = int(input('Antallet meter objektet skal ramle: '))
print(f'Det tar {get_fall_time(meter)} sekunder å ramle ned {meter} meter')