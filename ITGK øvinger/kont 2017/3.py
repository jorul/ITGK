def enter_line(prompt, length):
    linja = ''
    while len(linja) != length:
        linja = input(prompt)
        if len(linja) != length:
            print(f'The text must be {length} characters long')
    return linja

def adjust_string(text, length):
    if len(text) == length:
        return text
    elif len(text)>length:
        return text[:31]
    else:
        foran = (length-len(text))//2
        bak = (length-len(text))//2 + (length-len(text))%2
        for i in range(foran):
            text = f' {text}'
        for i in range(bak):
            text = f'{text} '
    return text

print('.', adjust_string("ITGK",30) ,'.')

def enter_line_smart(prompt, length):
    linje = input(prompt)
    return adjust_string(linje)

def enter_show_text():
    texten = []
    for i in range(1,7):
        linje = input(f'Line {i}: ')
        linje30 = adjust_string(linje, 30)
        texten.append(linje)
    show_display(texten)

import time
def scroll_display(content, line):
    linja = content[line-1]
    for i in range(30):
        first = linja[0]
        linja = linja[1:30] + first
        content[line-1] = linja
        show_display(content)
        time.sleep(0.1)

def display_from_file(filename):
    f = open(filename, 'r')
    liste = []
    for line in f:
        line = line.strip()
        line = adjust_string(line, 30)
        liste.append(line)
    for i in range (0,len(liste),6):
        aktuell_liste = liste[i:i+6]
        show_display(aktuell_liste)
        time.sleep(10)

        

