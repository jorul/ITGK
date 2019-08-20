from math import sqrt
GRAVITY = 9.81


def get_fall_time(x, *args):
    for i in args:
        t = sqrt(2*x/i)
        return t
    t = sqrt(2*x/GRAVITY)
    return t

print(get_fall_time(20))
print(get_fall_time(20,1.62))