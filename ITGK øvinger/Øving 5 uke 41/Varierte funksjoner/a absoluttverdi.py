def absol(x):
    if x>= 0:
        return x
    elif x < 0:
        return -x
    else:
        return 'slutt å tull'

tall = int(input('Hvilket tall vil du ha absoluttverdien til? '))
print(f"Absoluttverdien til {tall} er", absol(tall))