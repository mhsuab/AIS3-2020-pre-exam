from ctypes import *
from binascii import unhexlify
from Crypto.Util.number import bytes_to_long, long_to_bytes

def unsign(n):
  return c_uint(n).value

def cut(n):
  return n & 0xffffffff

a = input("> ")
a = unhexlify(a)
left, right = bytes_to_long(a[:4][::-1]), bytes_to_long(a[4:8][::-1])

keys = [b"Gold", b"Bort", b"Jade", b"Ruby"]
keys = [bytes_to_long(k) for k in keys]
#left = 0x31b8afa3
#right = 0xf34a68f7
#v6 = unsign(-1640531527)
print("Len", len(a))
print("Count", len(a)//8+1)
for _ in range(len(a)//8+1):
  v6 = unsign((-1640531527)*64)
  for _ in range(64):
    rL = unsign(((left >> 5) ^ cut(16*left)) + left)
    rR = unsign(keys[(v6>>11)&3] + v6)
    print(hex((rL ^ rR)), end=', ')
    right = unsign(right - (rL ^ rR))
    v6 = unsign(v6+1640531527)
    lL = unsign(((right >> 5) ^ cut(16*right)) + right)
    lR = unsign(keys[v6&3] + v6)
    left = unsign(left - (lL^lR))
    print(hex((lL^lR)))
    # if b"A" in long_to_bytes(left):
    print(long_to_bytes(left), long_to_bytes(right))

print(long_to_bytes(left)[::-1]+long_to_bytes(right)[::-1] + a[8:])