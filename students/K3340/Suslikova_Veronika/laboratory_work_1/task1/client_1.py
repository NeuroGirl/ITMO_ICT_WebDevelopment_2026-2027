import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'Hello, server!', ('localhost', 14901))
data, addr = sock.recvfrom(1024)
print(data.decode('utf-8'))