# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 02:09:45 2022

@author: me
"""
#import socket, select, sys

import socket
import time
#from timer import Timer

bufferSize  = 1024


localIP     = "127.0.0.1"

localPort   = 20002
RxMessage = ""
SenderAddr = ""
TimeoutTime = 15

#timer_time = time.Timer()

def receiveMessage(localIP, localPort, TimeoutTime):
    
    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    #Set non-blocking socket
    UDPServerSocket.setblocking(0)

    UDPServerSocket.settimeout(TimeoutTime)

    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))
    
    print("Starting listening on IP:{}, Port:{}".format(localIP, localPort))
    
    #start_time = time.time()
    wasMsgReceived = False
    wasTimeoutOccured = False
    
    #(time.time() - start_time < TimeoutTime) and
    while (not wasMsgReceived) and (not wasTimeoutOccured):

        try:

            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        
            RxMessage = bytesAddressPair[0]
        
            SenderAddr = bytesAddressPair[1]
        
            if RxMessage:
                Messag_ToPrint = "Message from Client:{}".format(RxMessage)
                SenderAddr_ToPrint  = "Client IP Address:{}".format(SenderAddr)
                
                print(Messag_ToPrint)
                print(SenderAddr_ToPrint)
        
                wasMsgReceived = True
                
        except socket.error:
            print("No data was received during timeout")
            wasTimeoutOccured = True
                 
    UDPServerSocket.close()
      
    return wasMsgReceived, RxMessage, SenderAddr
    
succeeded, RxMessage, SenderAddr= receiveMessage(localIP, localPort, 5)
