# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 02:09:45 2022

@author: me
"""
import socket, select, sys

#import socket
#import time
from timer import Timer

bufferSize  = 1024


localIP     = "127.0.0.1"

localPort   = 20001
RxMessage = ""
SenderAddr = ""
timer_time = Timer()

def receiveMessage(localIP, localPort, RxMessage, SenderAddr, TimeoutTime):
    
    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))
    
    UDPServerSocket.setdefaulttimeout(TimeoutTime)
    
    print("Starting listening on IP:{}, Port:{}".format(localIP, localPort))
    
    start_time = timer_time.start()
    
    while timer_time - start_time < TimeoutTime:

        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    
        message = bytesAddressPair[0]
    
        SenderAddr = bytesAddressPair[1]
    
        Messag_ToPrint = "Message from Client:{}".format(message)
        SenderAddr_ToPrint  = "Client IP Address:{}".format(SenderAddr)
        
        print(Messag_ToPrint)
        print(SenderAddr_ToPrint)
    
        #print(timer_time - start_time)
        
receiveMessage(localIP, localPort, RxMessage, SenderAddr, 5)



# serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

# serverSocket.setdefaulttimeout(6)

# serverSocket.bind(('localhost',localPort))
# running = True
# while running:    #running variable is set to True
#     incoming = select.select([serverSocket],[],[],5) #5 corresponds to timeout in seconds
#     try:
#         msg,sndr = incoming[0][0].recvfrom(2048)
#         print("{}, {}".format(msg, sndr))
#     except IndexError:
#         sys.stderr.write('Timed out in receiving message on UDP server')
#         continue