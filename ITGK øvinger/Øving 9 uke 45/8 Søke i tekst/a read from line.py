def read_from_file(filename):
    f = open(filename,'r')
    innhold = f.read()
    return innhold

def remove_symbols(text):
    text = str(text)
    text = text.lower()
    text = text.replace('\n','')
    text = text.replace('\t','')
    text = text.replace('.','')
    text = text.replace(',','')
    text = text.replace(':','')
    text = text.replace(';','')
    text = text.replace("'",'')
    text = text.replace("?",'')
    text = text.replace("!",'')
    text = text.replace("(",'')
    text = text.replace(")",'')
    for i in range(10):
        i = str(i)
        text = text.replace(i,'')
    return text

def count_words(filename):
    teller = {}
    teksten = remove_symbols(read_from_file(filename))
    lista = teksten.split(' ')
    for i in lista:
        try:
            teller[i] = teller[i] +1
        except:
            teller[i] = 1
    return teller


print(count_words('BIBLE.txt'))

'''
bible_dict = count_words('BIBLE.txt')
for word, value in bible_dict.items():
    print(word, value)
'''