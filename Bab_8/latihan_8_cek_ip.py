# Credit: Fikom UIT
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f"Hostname: {hostname}")
print(f"IP Address: {ip}")
