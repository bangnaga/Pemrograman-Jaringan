# Credit: Fikom UIT
import socket

def run_client():
    # 1. Membuat object socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Connect ke server
    host = 'localhost'
    port = 5000
    
    try:
        print(f"Mencoba menghubungkan ke {host}:{port}...")
        client_socket.connect((host, port))
        print("Terhubung!")
        
        # 3. Send data
        pesan = "Halo Server, ini Client Fikom!"
        client_socket.send(pesan.encode('utf-8'))
        
        # 4. Receive response
        data = client_socket.recv(1024)
        print(f"Respon Server: {data.decode('utf-8')}")
        
    except ConnectionRefusedError:
        print("Koneksi ditolak! Pastikan Server sudah berjalan.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # 5. Close
        client_socket.close()

if __name__ == "__main__":
    run_client()
