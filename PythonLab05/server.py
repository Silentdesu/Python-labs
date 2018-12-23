from socket import *
import os

HOST = '127.0.0.1'
PORT = 9999

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))
print("...waiting for message...")
while True:
	(data, address) = s.recvfrom(1024)
	print(data, address)
	if data.decode('utf-8') == 'bye': #If server will get 'bye' then recall 'bye' to client
		s.sendto('bye'.encode('utf-8'), address)
	if data.decode('utf-8') == 'dir': #If server will get 'dir' then print out all files in current directory
		for line in os.listdir():
			print(line)
	s.sendto('this is the UDP server'.encode('utf-8'), address)

s.close()