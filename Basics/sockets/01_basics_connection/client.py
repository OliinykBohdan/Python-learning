import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 8080))

text = 'Hello'

s.sendall(text.encode())
data = s.recv(1024)
print(data)

s.close()
