data = open("output", 'r').read()
data = data.split(" ")
data = [int(d) for d in data]
output = ["" for _ in range(64)]

for i in range(len(data)):
  if data[i] == 0:
    continue
  char = chr((i*45)%314)
  val = data[i]
  while val > 0:
    output[val%64] = char
    val = val >> 6

print("".join(output))