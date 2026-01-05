# Credit: Fikom UIT
import socket
import ssl

def secure_server():
    # Setup SSL Context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    try:
        context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
    except FileNotFoundError:
        print("Sertifikat belum ada! Jalankan latihan_13_gen_cert.py dulu.")
        return

    bindsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bindsocket.bind(('localhost', 10023))
    bindsocket.listen(5)
    print("=== Secure TLS Server Listening on 10023 ===")

    # Wrap socket biasa dengan SSL
    # server_side=True artinya socket ini berperan sebagai server
    with context.wrap_socket(bindsocket, server_side=True) as ssock:
        while True:
            try:
                conn, addr = ssock.accept()
                print(f"Secure connection from {addr}")
                
                data = conn.recv(1024).decode()
                print(f"Received: {data}")
                
                conn.send(f"Server Says: Validated & Encrypted!".encode())
                conn.close()
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    secure_server()
