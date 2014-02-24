import base64, getpass
from socket import *

endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "10.0.0.2" #Fill in start   #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
#Fill in end
recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'EHLO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

clientSocket.send("AUTH LOGIN\r\n")
recv1_1 = clientSocket.recv(1024)
print recv1_1

print "Enter Username"
user = raw_input()
clientSocket.send(base64.b64encode(user)+"\r\n")
recv1_2 = clientSocket.recv(1024)
print recv1_2

print "Enter Password"
psw = getpass.getpass()
clientSocket.send(base64.b64encode(psw)+"\r\n")
recv1_3 = clientSocket.recv(1024)
print recv1_3
recv1_4 = clientSocket.recv(1024)
print recv1_4
# Send MAIL FROM command and print server response.
# Fill in start
MAILFROM = "MAIL FROM: <"
print "Send mail from:"
sender = raw_input()
clientSocket.send(MAILFROM+sender+">\r\n")

recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
RCPTTO = "RCPT TO: <"
print "Send mail to:"
rcpt = raw_input()
clientSocket.send(RCPTTO+rcpt+">\r\n")

recv3 = clientSocket.recv(1024)
print recv3
if recv3[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Send DATA command and print server response.
# Fill in start
clientSocket.send("DATA\r\n")

recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != '354':
	print '354 reply not received from server.'
# Fill in end
clientSocket.send("To: "+sender+"\r\n")
clientSocket.send("From: "+rcpt+"\r\n")
print "Enter Subject:"
subj = raw_input()
clientSocket.send("Subject: "+subj+"\r\n\r\n")
# Send message data.
# Fill in start
print "Write message (end with \"END\"):"
while True:
	msg = raw_input()
	if msg == "END":
		break
	clientSocket.send(msg+"\r\n")
# Fill in end
# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg)
recv5 = clientSocket.recv(1024)
print recv5
if recv5[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send("QUIT\r\n")
recv6 = clientSocket.recv(1024)
print recv6
if recv5[:3] != '221':
	print '221 reply not received from server.'
# Fill in end
raw_input()