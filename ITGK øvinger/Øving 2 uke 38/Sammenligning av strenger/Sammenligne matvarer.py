mat1 = input('Matvare 1: ')
mat2 = input('Matvare 2: ')
print(f'Sammenligner {mat1} og {mat2}')
if str.lower(mat1) == str.lower(mat2):
    print('Dette er samme matvare')
else:
    print('Dette er to forskjellige matvarer')