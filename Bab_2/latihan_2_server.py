# Credit: Fikom UIT
import socket

def run_server():
    # 1. Membuat object socket
    # AF_INET = IPv4, SOCK_STREAM = TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Bind (Mengikat ke alamat IP dan Port)
    host = 'localhost' # Bisa juga '0.0.0.0' untuk menerima dari luar network
    port = 5000
    server_socket.bind((host, port))
    
    # 3. Listen (Mulai mendengarkan)
    # Angka 1 berarti antrian koneksi maksimum (backlog)
    server_socket.listen(1)
    print(f"Server berjalan di {host}:{port}, menunggu client...")
    
    # 4. Accept (Menerima koneksi - BLOCKING)
    # conn = objek socket baru khusus untuk client ini
    # addr = alamat client (ip, port)
    conn, addr = server_socket.accept()
    print(f"Koneksi diterima dari: {addr}")
    
    # 5. Receive & Send
    try:
        data = conn.recv(1024) # Buffer size 1024 bytes
        message = data.decode('utf-8')
        print(f"Client mengirim: {message}")
        
        reply = f"Server menerima: {message}"
        conn.send(reply.encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 6. Close connection
        conn.close()
        server_socket.close()
        print("Koneksi ditutup.")

if __name__ == "__main__":
    run_server()
