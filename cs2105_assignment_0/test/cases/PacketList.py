 
import sys

offin = 0
offout = 0

while True:
  buf = b''
  while not buf.endswith(b'B'):
    buf0 = sys.stdin.buffer.read1(1)
    if len(buf0) == 0:
      sys.exit()
    buf += buf0
  print('%d %d' % (offin, offout))
  s = int(buf[6:-1])
  offin += s + len(buf)
  offout += s
  while s > 0:
    b = sys.stdin.buffer.read1(s)
    s -= len(b)
    #sys.stderr.write(str(len(b)) + '\n')
  #buf = sys.stdin.buffer.read(s)
  #sys.stdout.buffer.write(buf)
