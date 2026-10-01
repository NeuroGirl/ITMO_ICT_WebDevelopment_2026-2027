import socket
import threading

nickname = input("Введите ник: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 14901))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("Соединение разорвано.")
            client_socket.close()
            break

recv_thread = threading.Thread(target=receive_messages)
recv_thread.daemon = True
recv_thread.start()

while True:
    text = input()
    message = f"От {nickname}: {text}"
    client_socket.sendall(message.encode())