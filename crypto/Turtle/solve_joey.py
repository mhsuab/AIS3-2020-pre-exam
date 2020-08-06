import requests
from base64 import b64decode, b64encode

host = "https://turtowl.ais3.org/?action=login"
token = "cahVtVSUyNaazoSUXUMm6VokO/b2k6C/r5TAso8/UKpNrtsRciw/DDXD+MhbLqcayQ/3QGsdzvqUw5k31GgLVA=="
token = b64decode(token)
iv, ct = token[:16], token[16:]
output = []

def bytes_xor(b1, b2):
  return bytes([b1[i]^b2[i] for i in range(len(b1))])

def list_xor(l1, l2):
  return [l1[i] ^ l2[i] for i in range(len(l1))]

def oracle(s, payload):
  payload = b64encode(payload)
  r = s.post(
    host, 
    cookies={'PHPSESSID': '35520e50165dcc606224f40aa6cb5499'}, 
    data={"csrf_token": payload, "username": 'a', 'password': 'a', "submit": "Login"}
  )
  if "invalid" in r.text:
    return True
  else:
    return False

def decrypt(ct, prev):
  s = requests.Session()
  mid = [0 for _ in range(16)]
  zeros = bytes([0 for _ in range(16)])
  for i in range(16):
    for j in range(256):
      mid[15-i] = j
      if oracle(s, zeros+bytes(mid)+ct):
        print(i)
        break
    if i != 15:
      mid = list_xor(mid, [(i+1)^(i+2) for _ in range(16)])
  return bytes_xor(bytes(list_xor(mid, [16 for _ in range(16)])), prev)

def test():
  s = requests.Session()
  oracle(s, token)
  input("asdf")
  tmp = list(token)
  tmp[-17] = 123
  oracle(s, bytes(tmp))
  input("asdf")
  tmp = list(token)
  tmp[-33] = 123
  oracle(s, bytes(tmp))

def main():
  for i in range(0, len(token), 16):
    print(decrypt(token[i+16:i+32], token[i:i+16]))

main()
# AIS3{5l0w_4nd_5734dy_w1n5_7h3_r4c3.}