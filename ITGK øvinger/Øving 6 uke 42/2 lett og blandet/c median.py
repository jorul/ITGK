import math
def median(i):
    i.sort()
    midterste_element = math.ceil(len(i)/2)-1
    return i[midterste_element]
print(median([1,2,4,5,7,9,10]))
print(median([1,4,2,5,3]))