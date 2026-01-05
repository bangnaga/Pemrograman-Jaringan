# Credit: Fikom UIT
import socket

def chat_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen(1)
    print("=== Chat Server (TCP) ===")
    print("Menunggu lawan bicara...")
    
    conn, addr = server.accept()
    print(f"Terhubung dengan {addr}")
    
    while True:
        try:
            # Terima pesan dari client
            data = conn.recv(1024).decode('utf-8')
            
            # Cek jika koneksi putus atau client bilang bye
            if not data or data.lower() == 'bye':
                print("\n[!] Client mengakhiri obrolan.")
                break
                
            print(f"\nClient: {data}")
            
            # Balas pesan
            response = input("Anda (Server): ")
            conn.send(response.encode('utf-8'))
            
            if response.lower() == 'bye':
                print("[!] Anda mengakhiri obrolan.")
                break
                
        except ConnectionResetError:
            print("\n[!] Koneksi diputus paksa oleh client.")
            break
            
    conn.close()
    server.close()

if __name__ == "__main__":
    chat_server()
