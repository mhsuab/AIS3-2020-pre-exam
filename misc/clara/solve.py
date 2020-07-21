import sys
import os
from struct import unpack
from itertools import cycle

def bxor(b1, b2): # use xor for bytes
    return bytes(a ^ b for a, b in zip(b1, cycle(b2)))

with open(sys.argv[1], 'rb') as f:
    raw = f.read()

till = 0
keyexchange = raw[till:till + 8]
till += 8
key = raw[till:till + 8]
till += 8
l = len(raw)

key = bxor(keyexchange, key)
print ('key =', key.decode())
keylength = len(key)

bytes_string = b''
CASE = 0

while till < l:
    if CASE == 0 or CASE == 2:
        n = unpack('<I', bxor(raw[till: till + 4], key))[0]
        till += 4
    else:
        bytes_string = bxor(raw[till: till + n], key)
        till += n
        if CASE == 1:
            filename = bytes_string.decode()
        else:
            with open(os.path.join(sys.argv[1][:2], filename), 'wb') as f:
                f.write(bytes_string)
        bytes_string = b''
    CASE = (CASE + 1) % 4