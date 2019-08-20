import random
s = []
t = []

for i in range(20):
    s.append(random.randrange(0,5,2))
    t.append(random.randint(0,5))


print('randrange(0,5,[2]): ', s)
print('randint(0,5):', t)
s.sort()
print(s)
print(s[0:1])
print()
u=[]
for o in range(20):
    u.append(random.random())

print(random.random())
print(u)

k = 'god dag'

print(random.choice(k))
print(k[0:7:2])
v= []
v=[[0]*4]*6
print(v)

f= [1,2,5,10,3,8,7,13]
f.sort()
f.pop(7)
print(f)
