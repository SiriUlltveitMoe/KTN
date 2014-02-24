'''
Created on 16. feb. 2014

@author: Anders Lima
'''
from socket import *
import array 
import time

try:
    n, timeout = [int(x) for  x in raw_input("Enter number of packets to send\nand timeout (default: [4,1]) : ").split()]
except Exception,e:
    n=4
    timeout = 1

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(timeout)

norecv = 0
st0 = time.clock()
times = array.array('f')

for i in range(n):
    msg = "Ping no {} to {}".format(i,serverName)
    st = time.clock()
    
    try:
        clientSocket.sendto(msg, (serverName, serverPort))
        modMsg, serverAddress = clientSocket.recvfrom(1024)
    except Exception,e:
        print "TIMEOUT ON PACKET {} AFTER {} sec".format(i,timeout)
        continue
    
    rt = time.clock()
    RTT = rt - st
    times.append(RTT)
    norecv = norecv + 1
    print "{} ANSWERED IN {:.3f} ms".format(modMsg,RTT*1000)
    
et = time.clock()
print "\nRecieved {} of {} ({:.2%}) packets in {:.3f} sec.\nAverage response time: {:.3f}\
 ms\nMaximum response time: {:.3f} ms\nMinimum response time: {:.3f} ms"\
 .format(norecv,n,(norecv/float(n)),(et-st0),(float(sum(times))/len(times))*1000,float(max(times)*1000),float(min(times)*1000))
