from socket import *
import sys

server = {}
port = int(sys.argv[1])
welcome_socket = socket(AF_INET, SOCK_STREAM)

welcome_socket.bind(('', port))

while 1:
	welcome_socket.listen(1)

	connection_socket, client_addr = welcome_socket.accept()
	print("Server is connecting on ", client_addr)
	
	chunk = b''
	bytes = connection_socket.recv(2048)
	chunk += bytes
	while len(chunk):
		while chunk.find(b'  ') == -1:
			bytes = connection_socket.recv(2048)
			chunk += bytes

		index = chunk.find(b'  ')
		header = chunk[:index]
		headers = header.split(b' ')

		path = headers[1]
		key = path[5:]
		if headers[0].lower() == b'post':
			for i in range(2, len(headers), 2):
				if headers[i].lower() == b'content-length':
					no = i
					break
			length = headers[no+1]
			body_length = int(length.decode())
			body = chunk[index+2:]
			num = len(body)
			while  num < body_length:
				bytes = connection_socket.recv(2048)
				body += bytes
				num += len(bytes)
			content = body [:body_length]
			chunk = body [body_length:]
			server[key] = content
			response = b'200 OK  '
		else:
			chunk = chunk[index+2:]
			if key in server:
				content = server[key]
				if headers[0].lower() == b'delete':
					server.pop(key)
				str = "200 OK content-length {}  ".format(len(content))
				response = str.encode() + content
			else:
				response = b"404 NotFound  "	

		connection_socket.send(response)
		#print(b"to client: ", response)

		if len(chunk) == 0:
			bytes = connection_socket.recv(2048)
			chunk += bytes

	connection_socket.close()
	server.clear()
