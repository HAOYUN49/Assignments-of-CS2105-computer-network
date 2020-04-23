from socket import *
import sys
import zlib

recvName = 'localhost'
recvPort = int(sys.argv[1])

sendSocket = socket(AF_INET, SOCK_DGRAM)

seq = b'0'
packet = sys.stdin.buffer.read(53)
while len(packet):
	packet = seq + packet
	checksum = str(zlib.crc32(packet))
	checksum = '0'*(10-len(checksum)) + checksum

	packet = checksum.encode() + packet

	while 1:
		sendSocket.sendto(packet, (recvName, recvPort))
		sendSocket.settimeout(0.05)
		try:
			received = sendSocket.recv(64)
		except:
			received = b''
		if received == b'ACK':
			break

	if seq == b'0':
		seq = b'1'
	else:
		seq = b'0'
	packet = sys.stdin.buffer.read(53)

sendSocket.close()
