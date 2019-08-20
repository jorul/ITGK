def load_bin(filename):
    try:
        f = open(filename, 'r')
        tekst = ''
        for linje in f:
            linje_txt = str(linje)
            tekst += linje_txt.strip()
        f.close()
        return tekst
    except:
        print(f'Error: Could not open file {filename}')
        return ''

def bin_to_dec(binary):
    dec = 0
    lengde = len(binary)
    for i in range(lengde):
        if binary[lengde-1-i] == '1':
            dec += 2**i
    return dec

def dec_to_char(dec):
    if dec < 0 or dec >31:
        return ''
    else:
        listami = [' ', ',', '.', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Æ', 'Ø', 'Å']
        return listami[dec]

def bin_to_txt(binstring):
    antall_bokstaver = int(len(binstring)/5)
    totaltext = ''
    for i in range(antall_bokstaver):
        start = int(i*5)
        slutt = int(i*5+5)
        boks_binstring = binstring[start:slutt]
        boks_dec = bin_to_dec(boks_binstring)
        boks = dec_to_char(boks_dec)
        totaltext += boks
    return totaltext

def main():
    print('Binary-to-text converter')
    b_file = input('Name of binaryfile to load from: ')
    bin_string = load_bin(b_file)
    txt = bin_to_txt(bin_string)
    t_file = input('Name of textfile to save to: ')
    try:
        t = open(t_file, 'w')
        t.write(txt)
        t.close()
        print('binary.txt has been converted and saved to out.txt')
        return
    except:
        print(f'Error: Could not write to file {t_file}')



