# Credit: Fikom UIT
import socket
import time

def sticky_packet_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5000))
    
    # CASE 1: Kirim pesan "nempel" (Sticky Packet)
    # Kita kirim banyak pesan sekaligus tanpa delay
    print("Mengirim 5 pesan sekaligus...")
    
    # Perhatikan: Setiap pesan DIAKHIRI '\n' sebagai delimiter
    paket_besar = ""
    for i in range(5):
        paket_besar += f"PesanKe-{i+1}\n"
    
    # Kirim sekaligus dalam satu kali send()
    # Di sisi jaringan, ini akan jadi satu blok data
    client.send(paket_besar.encode('utf-8'))
    
    # Baca balasan satu per satu
    socket_file = client.makefile('r', encoding='utf-8')
    try:
        for _ in range(5):
            response = socket_file.readline().strip()
            print(f"Jawab Server: {response}")
    except Exception as e:
        print(f"Error baca: {e}")
        
    client.close()

if __name__ == "__main__":
    sticky_packet_client()
