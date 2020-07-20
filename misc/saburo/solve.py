from pwn import *

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`|}~ '
print (len(chars))
host = '60.250.197.227'
port = 11001

flag = 'AIS3{A1r1ght_U_4r3_my_3n3nnies'
prev_time = 390
max_time = prev_time
count = 0

while '}' not in flag:
    add = ''
    for i in chars:
        try:
            print (i, end = '')
            s = remote(host, port)
            s.recvuntil('Flag: ')
            s.sendline(flag + i)
            time = int(s.recvline()[18:-15].decode())
            print (time, end='')
            if time > max_time:
                max_time = time
                add = i
        except:
            print (flag + i)
            add = i
            break
        s.close()
    print ('prev:', prev_time)
    print ('now:', max_time)
    print ('add:', add)
    print ((flag + add).encode())
    # j = input(flag + add)
    # if j == '\n':
    if max_time - 10 > prev_time:
        prev_time = max_time
        flag += add
        print ('flag:', flag)
    else:
        count += 1
        if count == 3:
            flag = flag[:-1]
            prev_time -= 10
            print ('prev:', prev_time)

# AIS3{A1r1ght_U_4r3_my_3n3nnies}