#a
my_first_list = []
for i in range (1,7):
    my_first_list.append(i)
print(my_first_list)

#b
print(my_first_list[len(my_first_list)-1])

#c
my_first_list[len(my_first_list)-2]= 'pluss'
print(my_first_list)

#d
my_second_list = my_first_list[3:]
print(my_second_list)

#e
print(f'{my_second_list} er lik 10')