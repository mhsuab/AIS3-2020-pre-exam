import os
import pickle
import random
from base64 import b64decode, b64encode
from Crypto.Util import Counter
from Crypto.Cipher import Blowfish
from pwn import *
import sys

def bxor(b1, b2): # use xor for bytes
    return bytes(a ^ b for a, b in zip(b1, b2))

def pad(m):
    length = 8-len(m)%8
    return m+chr(length).encode()*length

pick = int(sys.argv[1])

obj = [{'name': 'maojui', 'password': 'SECRET', 'admin': False}, 
    {'name': 'djosix', 'password': 'S3crE7', 'admin': False}, 
    {'name': 'kaibro', 'password': 'GGInIn', 'admin': False}, 
    {'name': 'others', 'password': '_FLAG_', 'admin': False}]
obj_new = [{'name': 'maojui', 'password': 'SECRET', 'admin': False}, 
    {'name': 'djosix', 'password': 'S3crE7', 'admin': False}, 
    {'name': 'kaibro', 'password': 'GGInIn', 'admin': False}, 
    {'name': 'others', 'password': '_FLAG_', 'admin': False}]
obj_new[pick]['admin'] = True
print (obj_new)

p = pickle.dumps(obj) # .encode()
p_new = pickle.dumps(obj_new) # .encode()

for i in range(len(p_new)):
    if p[i] != p_new[i]:
        x = i
        print ('x', x)

username = obj[pick]['name']
password = obj[pick]['password']
TOKEN = ''

s = remote('192.168.56.103', 1346)
s.recvuntil('Your token: ')
token = s.recvline()[:-1]
oldTOKEN = b64decode(token)
print ('oldToken', len(oldTOKEN))
print (token)
TOKEN = bxor(bxor(oldTOKEN, p), p_new)
TOKEN = b64encode(TOKEN)
print (TOKEN)
print ()
    

s.recvuntil('username : ')
s.sendline(username)
s.recvuntil('password : ')
s.sendline(password)
s.recvuntil('TOKEN : ')
s.sendline(TOKEN)
s.recvline()
for _ in range(3):
    print (s.recvline().decode(), end = '')