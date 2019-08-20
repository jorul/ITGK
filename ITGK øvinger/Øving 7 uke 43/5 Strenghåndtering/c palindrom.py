def reversed_word(str):
    ordet =''
    for i in range(len(str)-1,-1,-1):
        ordet += str[i]
    return ordet

def check_palindrome(str1):
    str2 = reversed_word(str1)
    return str1 == str2


str1 = 'agnes i senga'
str2 = 'hello'
print(check_palindrome(str1))
print(check_palindrome(str2))