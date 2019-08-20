import binascii

def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)

def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def toBinary(word):
    return bytes(word, encoding = 'ascii')


def encrypt(message,key):
    heksmess = toHex(toBinary(message))
    hekskey = toHex(toBinary(key))
    return heksmess ^ hekskey

def decrypt (code, key):
    hekskey = toHex(toBinary(key))
    return toString( code ^ hekskey)


import random
def main():
    melding = input('Hva er meldingen? ')
    key = str(random.shuffle(list(melding)))
    krypto = encrypt(melding,key)
    print(f'Krypto: {krypto}')
    dekrypto = decrypt(krypto,key)
    print(f'Meldingen: {dekrypto}')

main()