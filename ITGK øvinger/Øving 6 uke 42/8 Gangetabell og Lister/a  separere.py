def separate (numbers, threshhold):
    under = []
    over = []
    for i in range(len(numbers)):
        if numbers[i]< threshhold:
            under.append(numbers[i])
        else:
            over.append(numbers[i])
    return under, over
print(separate([0,5,7,3,2,7,9,3], 6))