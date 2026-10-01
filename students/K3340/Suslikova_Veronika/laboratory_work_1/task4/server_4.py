import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 14901))
sock.listen()

clients = []

def send_message(message, sender):
    for c in clients:
        if c != sender:
            try:
                c.sendall(message)
            except:
                clients.remove(c)

def handle_client(client):
    while True:
        message = client.recv(1024)
        if not message:
            break
        send_message(message, client)

    clients.remove(client)
    client.close()

while True:
    client, addr = sock.accept()
    clients.append(client)
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()