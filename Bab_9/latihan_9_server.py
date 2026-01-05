# Credit: Fikom UIT
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(5)
print("Server listening on port 9999")

while True:
    client, addr = server.accept()
    print(f"Connection from {addr}")
    client.send(b"Halo dari Server!")
    client.close()
