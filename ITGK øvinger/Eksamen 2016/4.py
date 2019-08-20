D = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',6: 'six',7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',15: 'fifteen', 16: 'sixteen', 17: 'seventeen',18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',80: 'eighty', 90: 'ninety'}
L = [ 1000000, ' million', 1000, ' thousand', 1, '']



def i2_txt(tall):
    if tall < 20:
        return D[tall]
    else:
        tier = (tall // 10) * 10
        ener = tall % 10
        if ener != 0:
            return f'{D[tier]}-{D[ener]}'
        else:
            return D[tier]

def i3_txt(tall):
    if len(str(tall)) < 3:
        return i2_txt(tall)
    else:
        hundrer = tall //100
        resten = tall - hundrer*100
        if resten == 0:
            return f'{D[hundrer]} hundred'
        else:
            resten_txt = i2_txt(resten)
            return f'{D[hundrer]} hundred {resten}'

def i9_txt(tall):
    if len(str(tall)) <4:
        return i3_txt(tall)
    else:
        millioner = tall // 1000000
        tusner = (tall%1000000)//1000
        resten = tall - millioner * 1000000 - tusner*1000
        if tusner == 0:
            if resten == 0:
                millioner_txt = i3_txt(millioner)
                return f'{millioner_txt} million'
            else:
                resten_txt = i3_txt(resten)
                millioner_txt = i3_txt(millioner)
                return f'{millioner_txt} million {resten_txt}'
        elif millioner == 0:
            if resten == 0:
                tusner_txt = i3_txt(tusner)
                return f'{tusner_txt} thousand'
            else:
                resten_txt = i3_txt(resten)
                tusner_txt = i3_txt(tusner)
                return f'{tusner_txt} thousand {resten_txt}'
        elif resten == 0:
            millioner_txt = i3_txt(millioner)
            tusner_txt = i3_txt(tusner)
            return f'{millioner_txt} million {tusner_txt} thousand'
        else:
            resten_txt = i3_txt(resten)
            millioner_txt = i3_txt(millioner)
            tusner_txt = i3_txt(tusner)
            return f'{millioner_txt} million {tusner_txt} thousand {resten_txt}'

def add_words(tekststreng):
    tallindexer = []
    liste = tekststreng.split()
    for i in range(len(liste)):
        try:
            tall = int(liste[i])
            tallindexer.append(i)
        except:
            tallindexer = tallindexer
    nystreng = ''
    index = 0
    while index < len(liste):
        if index not in tallindexer:
            nystreng += (liste[index] + ' ')
            index += 1
        else:
            nystreng += (liste[index] + ' ')
            tall_txt = i9_txt(int(liste[index]))
            nystreng += '- ' + tall_txt + ' - '
            index +=1
    return nystreng.strip()

print(add_words('C owes 91 pounds to D and 55 pounds to E'))