from string import printable
from subprocess import check_output
from Crypto.Util.number import long_to_bytes
from itertools import product

with open('flag', 'r') as f:
    target = f.readlines()[-1]

s = (b'AIS3{' + b'000' + long_to_bytes(int(target, 16))[8:]).decode()
target = target.encode()
possible = printable[:-5]

for p in product(possible, repeat = 3):
    flag = s[:5] + ''.join(p) + s[8:]
    print (flag, end='\r')
    c = check_output('./Long_Island_Iced_Tea', input = flag.encode(), shell = True).split(b'\n')[-1]
    if c == target:
        print ('flag:', flag)
        break