import sys
ip = sys.argv[1]
binary = [int(ip[:8]), int(ip[8:16]), int(ip[16:24]), int(ip[24:])]
decimal = [None]*4
for index, number in enumerate(binary):
	no = 0
	for i in range(8):
		remainder = number%10
		number //= 10
		no += remainder * pow(2, i)
	decimal[index] = str(no)
seq = '.'
print(seq.join(decimal))
