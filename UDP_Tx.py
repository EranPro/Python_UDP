# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 01:43:50 2022

@author: me
"""
import socket
import time

Payload = "Hello UDP Server"
DesAddr = ("127.0.0.1", 20002)



def sendMessage(Payload, DesAddr, NumOfTimes, Delay):
    bytesToSend = str.encode(Payload)
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    for Num in range(NumOfTimes):
        print("Sending msg# {}/{}".format(Num+1, NumOfTimes))
        
        try:
            UDPClientSocket.sendto(bytesToSend, DesAddr)
        except Exception as e:
            print("==== Warning==== Failed to send msg# {}/{}. Failure reason:{}".format(Num+1, NumOfTimes, e))    
        
        time.sleep(Delay)
        
sendMessage(Payload, DesAddr, 4, 2)