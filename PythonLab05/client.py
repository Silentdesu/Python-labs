from socket import *

HOST = '127.0.0.1'
PORT = 9999
DETERMINATE = True

s = socket(AF_INET, SOCK_DGRAM)
s.connect((HOST, PORT))

while DETERMINATE:
	message = input('send message: ')

	s.sendall(message.encode('utf-8'))
	data = s.recv(1024)
	print(data)
	if data == 'bye'.encode('utf-8'): #When you'll get from server 'bye' then your client will determinate
		DETERMINATE = False

s.close()