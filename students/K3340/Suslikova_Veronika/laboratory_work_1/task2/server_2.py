import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 14901))
sock.listen(10)
client, addr = sock.accept()
data = client.recv(1024).decode('utf-8').split()
response = (int(data[0]) + int(data[1])) * int(data[2]) / 2
print(response)
client.send(str(response).encode('utf-8'))
sock.close()