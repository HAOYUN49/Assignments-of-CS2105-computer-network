import sys

data = sys.stdin.buffer.read1(6)
while not len(data) == 0:
	size = b''
	data = sys.stdin.buffer.read1(1)
	while data.find(b'B') == -1:
		size += data
		data = sys.stdin.buffer.read1(1)
	size_num = int(size)
	byte = sys.stdin.buffer.read(size_num)
	sys.stdout.buffer.write(byte)
	sys.stdout.buffer.flush()
	data = sys.stdin.buffer.read(6)
