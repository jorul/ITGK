my_family = {}
def add_family_member(role,name):
    if role not in my_family:
        my_family[role] = [name]
    else:
        liste = my_family[role]
        liste.append(name)
        my_family[role] = liste

add_family_member('bror', 'Arne')
add_family_member('mor', 'Anne')
add_family_member('bror', 'Geir')

for rolle in my_family :
    print (rolle, end = ': ')
    for medlem in my_family[rolle]:
        print(medlem, end =', ')
    print()




'''
ans = ' '
while ans != '':
    ans = input('Navn på et familiemedlem: ')
    if ans == '':
        break
    role = input('Deres rolle: ')
    add_family_member(role,ans)
print (my_family)
'''