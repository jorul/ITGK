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

key = 'abc'
msg = 'hei'

print(encrypt(key,msg))