# Credit: Fikom UIT
import socket

def chat_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("=== Chat Client (TCP) ===")
    
    try:
        client.connect(('localhost', 5000))
        print("Terhubung ke Server! Silakan kirim pesan.")
        
        while True:
            # Kirim pesan duluan
            pesan = input("Anda (Client): ")
            client.send(pesan.encode('utf-8'))
            
            if pesan.lower() == 'bye':
                print("[!] Anda mengakhiri obrolan.")
                break
            
            # Tunggu balasan server
            print("Menunggu balasan server...")
            response = client.recv(1024).decode('utf-8')
            
            if not response or response.lower() == 'bye':
                print("\n[!] Server mengakhiri obrolan.")
                break
                
            print(f"\nServer: {response}")
            
    except ConnectionRefusedError:
        print("[!] Gagal connect. Server belum nyala?")
    except ConnectionResetError:
        print("\n[!] Koneksi terputus.")
    finally:
        client.close()

if __name__ == "__main__":
    chat_client()
