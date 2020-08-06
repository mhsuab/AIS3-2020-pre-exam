table = '56789{}_WXY0yzABabcdmnopSTUVGHIJKLMNuvwxefghqrstijklOPQRCDEF1234'
with open('TsaiBroSaid', 'r') as f:
    f.readline()
    s = f.readline()
l = [len(i) for i in s.split('發財')[1:]]
print (''.join(table[8 * (l[2 * j] - 1) + l[2 * j + 1] - 1] for j in range(len(l)//2)))

# FLAG : AIS3{y3s_y0u_h4ve_s4w_7h1s_ch4ll3ng3_bef0r3_bu7_its_m0r3_looooooooooooooooooong_7h1s_t1m3}