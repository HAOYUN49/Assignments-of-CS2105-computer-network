from socket import *
import sys
import zlib

def compute_check(packet):
	checksum = packet[:10]
	packet = packet[10:]
	check = str(zlib.crc32(packet))
	check = '0'*(10-len(check))+check
	return (checksum.decode(), check)

def receive_packet():
	packet, sendAdd = recvSocket.recvfrom(64)
	checksum, check = compute_check(packet)
	while not checksum == check:
		recvSocket.sendto(b'NAK', sendAdd)
		packet, sendAdd = recvSocket.recvfrom(64)
		checksum, check = compute_check(packet)
	recvSocket.sendto(b'ACK', sendAdd)
	return (packet[10:11], packet[11:])


recvPort = int(sys.argv[1])

recvSocket = socket(AF_INET, SOCK_DGRAM)

recvSocket.bind(('', recvPort))

seq = b'0'

while 1:
	seq_num, packet = receive_packet()
	if seq_num == seq:
		sys.stdout.write(packet.decode())
		if seq == b'0':
			seq = b'1'
		else:
			seq = b'0'
