import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 14901))
data, addr = sock.recvfrom(1024)
udata = data.decode('utf-8')
print(udata)
sock.sendto(b'Hello, client!', addr)
sock.close()