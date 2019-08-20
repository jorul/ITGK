def contains_string(str1,str2):
    s = -1
    for i in range (len(str1)):
        for t in range(1,len(str1)+1):
            strengen = str1[i:t]
            if strengen== str2:
                s = i
    return s



str1 = 'pepperkake'
str2 = 'per'
str3 = 'ola'
print(contains_string(str1, str2))
print(contains_string(str1, str3))