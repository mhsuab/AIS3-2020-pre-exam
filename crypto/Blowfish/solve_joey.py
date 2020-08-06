from pwn import *
from base64 import b64decode, b64encode
import pickle

host = "localhost"
host = "60.250.197.227"
port = 12001

pt = ""
with open("user.pickle", 'rb') as infile:
  pt = infile.read()

s = remote(host, port)
s.recvuntil("Your token: ", timeout=1)
ct = b64decode(s.recvline())
assert len(pt) == len(ct)
key_stream = []
for i in range(len(pt)):
  key_stream.append(pt[i]^ct[i])
payload = [{'name': 'a', 'password': 'a', 'admin': True}]
pt = pickle.dumps(payload)
assert len(pt) < len(key_stream)
ct = b""
for i in range(len(pt)):
  ct += bytes([pt[i]^key_stream[i]])
output = b64encode(ct)

s.recvuntil("username : ", timeout=0.1)
s.sendline("a")
s.recvuntil("password : ", timeout=0.1)
s.sendline("a")
s.recvuntil("TOKEN : ", timeout=0.1)
s.sendline(output)
s.interactive()