from math import exp
def f(x):
    return (x-12)*exp(x/2)-8*(x-2)**2
def g(x):
    return -x-2*x**2-5*x**3+6*x**4
print(f(0))
print(g(1))