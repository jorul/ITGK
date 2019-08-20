def number_of_lines(filename):
    f = open(filename, 'r')
    count = len(f.readlines())
    return count
print(number_of_lines('numbers.txt'))

def number_frequency(filename):
    teller = {}
    file = open(filename, 'r')
    for line in file:
        tallet = line[0]
        try:
            teller[tallet] = teller[tallet] + 1
        except:
            teller[tallet] = 1
    file.close()
    return teller

print(number_frequency('numbers.txt'))

teller = number_frequency('numbers.txt')
for key,val in teller.items():
    print (f'{key}: {val}')