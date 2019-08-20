import random
def make_vec():
    listami = []
    for i in range (3):
        listami.append(random.randint(-10,11))
    return listami
print(make_vec())

