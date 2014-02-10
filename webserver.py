#import socket module

from socket import * 

serverSocket = socket(AF_INET, SOCK_STREAM) 

#Prepare a sever socket 

#Fill in start 
serverPort = 9999
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Server is ready to recieve...")
#Fill in end 

while True: 
	#Establish the connection 
	print 'Ready to serve...' 
 	connectionSocket, addr = serverSocket.accept() 
 	try: 
 		message = connectionSocket.recv(1024)#Fill in start #Fill in end 
 		print(message)
 		filename = message.split()[1]
 		print(filename)
 		f = open(filename[1:]) 
 		outputdata = f.readlines()#Fill in start #Fill in end 
	 	#Send one HTTP header line into socket 
	 	#Fill in start 
	 	OK = "HTTP/1.1 200 OK\n\n"
	 	connectionSocket.send(OK)
	 	#Fill in end 
	 	#Send the content of the requested file to the client 
	 	for i in range(0, len(outputdata)): 
	 		connectionSocket.send(outputdata[i]) 
	 	connectionSocket.close() 
	except IOError: 
		#Send response message for file not found 
		#Fill in start 
		NOT_FOUND = "HTTP/1.1 404 NOT FOUND\n\n"
		connectionSocket.send(NOT_FOUND);
		
		f = open("404.html")
		outputdata = f.readlines()
		#Fill in end 0
		for i in range(0, len(outputdata)): 
	 		print(outputdata[i])
	 		connectionSocket.send(outputdata[i]) 
		#Close client socket 
		#Fill in start 
		connectionSocket.close()
		#Fill in end
serverSocket.close() 