import random
listami = []
for i in range(100):
    listami.append(random.randint(1,10))

print(f'Number of 2s: {listami.count(2)}')

print(f'Sum of numbers: {sum(listami)}')

print(f'Numbers sorted: {sorted(listami)}')

import collections
data = collections.Counter(listami)
typetall = data.most_common()
print(f'There are most of number: {typetall[0][0]}')

print(f'Numbers reversed: {sorted(listami)[::-1]}')