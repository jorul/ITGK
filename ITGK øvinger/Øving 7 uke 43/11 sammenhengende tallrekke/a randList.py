import random
def randList(size, lower_bound, upper_bound):
    listami = []
    for i in range(size):
        listami.append(random.randint(lower_bound,upper_bound))
    return listami

def compareLists(list1,list2):
    liketall = []
    for i in range (len(list1)):
        for j in range (len(list2)):
            if list1[i]==list2[j] and list1[i] not in liketall:
                liketall.append(list1[i])
    return sorted(liketall)

def multiCompList(lists):
    sammenligningen = lists[0]
    for i in lists[1:]:
        sammenligningen = compareLists(sammenligningen,i)
    return sammenligningen


def longestEven(liste):
    biggestlist = 0
    currentlist = 0
    biggestindex = False
    currentbiggestindex = False
    for i in range(len(liste)):
        if (liste[i])%2 ==0:
            if currentlist == 0:
                currentbiggestindex = i
            currentlist += 1
            if currentlist > biggestlist:
                biggestlist = currentlist
                biggestindex = currentbiggestindex
        else:
            currentlist = 0
    return (biggestindex, biggestlist)

def main():
    print(randList(10,2,7))
    a = [1,2,3]
    b = [4,3,1]
    print(compareLists(a,b))
    c = [7,2,1]
    d = [a,b,c]
    print(multiCompList(d))
    liste = [4,3,3,6,2,6,8,3,4,3,3]
    print(longestEven(liste))

main()

