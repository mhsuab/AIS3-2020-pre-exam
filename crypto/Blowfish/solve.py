import pickle
from base64 import b64encode, b64decode
from Crypto.Util import Counter
from pwn import *

host = '192.168.56.103'
port = 1346
pick = 0

def bxor(b1, b2): # use xor for bytes
    return bytes(a ^ b for a, b in zip(b1, b2))

def exploit(s):
    p = open('user.pickle', 'rb').read()
    obj = pickle.loads(p)
    obj[pick]['admin'] = True

    adj_p = pickle.dumps(obj)
    print (type(adj_p))

    for i in range(len(p)):
        if p[i] != adj_p[i]:
            x = i
    
    username = obj[pick]['name']
    password = obj[pick]['password']

    TOKEN = ''
    s.recvuntil('Your token: ')
    token = s.recvline()[:-1]
    oldTOKEN = b64decode(token)
    TOKEN = bxor(bxor(oldTOKEN, p), adj_p)
    TOKEN = b64encode(TOKEN)

    s.recvuntil('username : ')
    s.sendline(username)
    s.recvuntil('password : ')
    s.sendline(password)
    s.recvuntil('TOKEN : ')
    s.sendline(TOKEN)
    s.recvline()
    for _ in range(3):
        print (s.recvline().decode(), end = '')

if __name__ == "__main__":
    s = remote(host, port)
    exploit(s)