raw = []
with open('prob', 'r') as f:
    chars = f.readline()[:-1].replace(' ', '')
    for i in f.readlines():
        if i != '\n':
            raw.append(i)

d = {i:i for i in '{}_'}
for i in range(len(chars)):
    tmp = raw[i][:-1].replace(' ', '')
    for j, k in zip(tmp[1:], chars):
        d[k + tmp[0]] = j
# print (d)

ct = raw[-1].split(' ')
flag = [d[i] for i in ct]
print (''.join(i for i in flag))