import socket
import time

if __name__ == "__main__":

	HOST='192.168.10.105'
	PORT=14000
	BUFSIZE=1024
	ADDR=(HOST, PORT)

	tcpCliSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcpCliSock.connect(ADDR)

	while True:
		tcpCliSock.send(b'#14P500T500\r\n')
		#data=tcpCliSock.recv(BUFSIZE)
		#print(data)
		time.sleep(0.5)
		
		tcpCliSock.send(b'#14P1500T500\r\n')
		time.sleep(0.5)
		
		tcpCliSock.send(b'#13P500T500\r\n')
		time.sleep(0.5)
		
		tcpCliSock.send(b'#13P1500T500\r\n')
		time.sleep(0.5)
		
		tcpCliSock.send(b'#15P500T500\r\n')
		time.sleep(0.5)
		
		tcpCliSock.send(b'#15P1500T500\r\n')
		time.sleep(0.5)
		
		tcpCliSock.send(b'#16P500T500\r\n')
		time.sleep(0.5)
		
		tcpCliSock.send(b'#16P1500T500\r\n')
		time.sleep(0.5)