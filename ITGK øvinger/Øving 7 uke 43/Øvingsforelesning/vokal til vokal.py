def funnyword(word):
    new_word = ''
    vokaler = ['a', 'e', 'i', 'u', 'o', 'y', 'æ', 'ø', 'å']
    import random
    for letter in word:
        if letter in vokaler:
            new_word += random.choice(vokaler)
        else: 
            new_word += letter
    return new_word

print(funnyword('tidenes funksjon'))