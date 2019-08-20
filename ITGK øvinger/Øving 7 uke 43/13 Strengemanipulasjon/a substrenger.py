def substring(str2,str1):
    str1 = str1.lower()
    str2 = str2.lower()

    s = -1
    if s == -1:
        s = []

    for i in range (len(str1)):
        for t in range(1,len(str1)+1):
            strengen = str1[i:t]
            if strengen== str2:
                s.append(i)
    return s

str1 = "oo"
str2 = "Never let you go let me go. Never let me go ooo"
print(substring(str1,str2))