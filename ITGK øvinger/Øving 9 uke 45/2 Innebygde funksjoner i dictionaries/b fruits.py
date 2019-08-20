fruit = {'epler': 2, 'pærer': 3, 'appelsiner': 1}

fruit['bananer'] = 0
fruit['druer'] = 1

del fruit['epler']
del fruit['pærer']
del fruit['appelsiner']

for val in fruit.values():
    print (val)

if 'bananer' in fruit:
    del fruit['bananer']

print(fruit)

fruit['jordbær'] = 2
fruit ['blåbær'] = 8
for key,val in fruit.items():
    print(key,val)