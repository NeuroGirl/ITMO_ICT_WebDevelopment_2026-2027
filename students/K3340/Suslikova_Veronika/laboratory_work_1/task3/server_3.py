import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 14901))
sock.listen(10)

print(f"HTTP сервер запущен на http://localhost:14901 ...")

data = open('students/K3340/Suslikova_Veronika/laboratory_work_1/task3/index.html', 'r', encoding='utf-8').read()

while True:
    client, addr = sock.accept()
    response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=UTF-8\r\n"
            f"Content-Length: {len(data.encode('utf-8'))}\r\n"
            "\r\n"
            + data
        )
    client.send(response.encode('utf-8'))
    client.close()