number_list = []
for i in range(100):
    number_list.append(i)

summen = 0
for i in range (len(number_list)):
    if number_list[i]%3 == 0 or number_list[i]%10 == 0:
        summen += number_list[i]
print (summen)