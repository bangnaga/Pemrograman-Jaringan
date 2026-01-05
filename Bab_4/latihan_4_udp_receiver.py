# Credit: Fikom UIT
import socket

def udp_receiver():
    # Perhatikan: SOCK_DGRAM untuk UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Tetap perlu bind agar bisa menerima data di port tertentu
    ip = 'localhost'
    port = 9999
    try:
        sock.bind((ip, port))
        print(f"UDP Server Listening on {ip}:{port}")
        
        while True:
            # recvfrom mengembalikan (data, address_pengirim)
            # Berbeda dengan recv() TCP yg cuma return data
            data, addr = sock.recvfrom(1024)
            print(f"[{addr}] Data Masuk: {data.decode('utf-8')}")
            
    except KeyboardInterrupt:
        print("\nServer dihentikan.")
    finally:
        sock.close()

if __name__ == "__main__":
    udp_receiver()
