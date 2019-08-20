def substring(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()

    s = []

    for i in range (len(str2)):
        for t in range(1,len(str2)+1):
            if str2[i:t] == str1:
                s.append(i)
    return s

def byttut(str1, str2, str3):
    indexene = substring(str1,str2)
    str2.lower()
    str3.lower()
    nystr = ""
    skip = 0
    for index, letter in enumerate(str2):
        if index not in indexene:
            if skip != 0:
                skip -= 1
            else:
                nystr = nystr + letter
        else:
            nystr = nystr + str3
            skip = len(str1)-1

    #for index in indexene[::-1]:
        #str2 = str2[:index] + str3 + str2[index+len(str1):]


    return nystr

str1 = "oo"
str2 = "Never let you goooo let me goo. Never let me goo oooo" 
str3 = "cool"
print(byttut(str1,str2,str3))

str1 = "iS"
str2 = "Is this the real life? Is this just fantasy?"
str3 = "cool"
print(byttut(str1,str2,str3))

str1 = 'fisk'
str2 = 'Vi skal ha fisk til middag.'
str3 = 'pannekake' 

print(byttut(str1,str2,str3))