# Credit: Fikom UIT
import socket
import threading

# Kita gunakan thread hanya untuk menerima pesan agar input user tidak terganggu
# Client ini sederhana saja, fokus utama bab ini ada di Server.

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data: break
            print(f"\n{data.decode()}\nAnda: ", end="")
        except:
            break

def run_simple_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('localhost', 9000))
    except:
        print("Gagal connect. Server mati?")
        return

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    print("Terhubung ke Chat Room! Ketik pesan Anda:")
    while True:
        try:
            msg = input("Anda: ")
            client.send(msg.encode())
        except KeyboardInterrupt:
            break
            
    client.close()

if __name__ == "__main__":
    run_simple_client()
