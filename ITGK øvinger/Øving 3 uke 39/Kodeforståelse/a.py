a=345
b=''
while a or b=='':
    b=str(a%2)+b
    a=a//2
print(b)