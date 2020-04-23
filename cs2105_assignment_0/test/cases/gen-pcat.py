 
import sys
import os
import random
import base64

specs = [
  {'np': 10, 'psize': 100000}, 
  {'np': 10000, 'psize': 100}, 
  {'np': 1, 'psize': 10000000}, 
  {'np': 1000, 'psize': 0}, 
  {'np': 1000, 'psize': 1}, 
]

genbytes = [
  lambda s: bytes(s), 
  lambda s: os.urandom(s), 
  lambda s: base64.b64encode(os.urandom(s))[:s]
]

def genFile(np, psize, f, genbytes):
  for i in range(np):
    s = random.randint(psize//2, psize)
    f.write(b'Size: ' + str(s).encode() + b'B')
    f.write(genbytes(s))

i = 1
for spec in specs:
  for gen in genbytes:
    with open('%d.in' % i, 'wb') as f:
      genFile(f=f, genbytes=gen, **spec)
    i += 1
