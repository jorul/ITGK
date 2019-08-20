f = open('minfil.txt')
def write_to_file(data):
    f = open('minfil.txt','w')                #w spesifiserer at filen skal skrives til
    f.write(data)
    f.close()

def read_from_file(filename):
    f = open(filename,'r')
    innhold = f.read()
    print(innhold)
    f.close()

def main():
    todo =''
    while todo != 'done':
        todo = input('Do you want to read or write? ')
        if todo == 'write':
            data = input('What do you want to write to file? ')
            write_to_file(data)
            print(f'{data} was written to file.')
        elif todo == 'read':
            read_from_file('minfil.txt')
    print('You are done.')

main()
