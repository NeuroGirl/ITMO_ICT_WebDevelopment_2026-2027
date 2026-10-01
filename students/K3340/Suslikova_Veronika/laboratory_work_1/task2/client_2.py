import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 14901))
task = input('Введите a b h трапеции: ')
sock.send(task.encode('utf-8'))
data = sock.recv(1024).decode('utf-8')
print(data)
sock.close()