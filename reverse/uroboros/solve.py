target = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 511847092 0 0 0 0 0 0 48 0 0 0 0 0 0 0 40984114273074 0 0 0 0 0 280 0 0 0 0 0 0 26022 26 0 0 0 0 0 0 2035 0 0 0 0 0 0 15 0 0 0 0 0 0 53 0 0 0 0 0 0 47 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 42350 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 40 0 0 0 0 0 0 29201 0 0 0 0 0 0 805 0 0 0 0 0 1 939 0 0 0 0 0 0 13 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 7739889 0 0 0 0 0 0 1251 0 0 0 0 0 0 45 0 0 0 0 0 0 2950300 0 0 0 0 0 2 23 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 54 0 0 0 0 0 0 0 0 0 0 0 0 0 5 0 0 0 0 0 0 0 0 0 0 0 0 0 55 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 '
target = [int(i) for i in target.split(' ')[:-1]]
flag = ['' for _ in range(100)]

from sympy import mod_inverse

inv_7 = mod_inverse(7, 314)
for idx, value in enumerate(target):
    while value:
        c = chr((idx * inv_7) % 314)
        flag[value & 0b111111] = c
        value = value >> 6
print (''.join(i for i in flag))


