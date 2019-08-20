def flopp(mat):
    r = len(mat)
    c = len(mat[0])
    for i in range(r):
        for j in range(c):
            if mat[i][j] == 1:
                mat[i][j] = 0
            else:
                mat[i][j] = 1
    return mat
def main():
    M = [ [0, 1, 0], [1, 0, 1], [0, 1, 0] ]
    print(flopp(M))

main()

x = 1
y = 'n'
print(x,y)

print(int(3215.5))

jaja = 'jaja' + 'hei'
print(jaja)

binstring= '00011'
print(binstring[0,1])