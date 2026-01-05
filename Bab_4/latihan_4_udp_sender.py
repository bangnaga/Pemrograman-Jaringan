# Credit: Fikom UIT
import socket
import time
import random

def udp_sender():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # UDP tidak perlu connect()
    target_ip = 'localhost'
    target_port = 9999
    target_addr = (target_ip, target_port)
    
    print(f"Mulai mengirim data dummy ke {target_addr}...")
    print("Tekan Ctrl+C untuk berhenti.")
    
    try:
        packet_count = 0
        while True:
            packet_count += 1
            # Simulasi data sensor
            suhu = random.randint(20, 40)
            kelembapan = random.randint(40, 80)
            
            payload = f"#{packet_count} | Suhu: {suhu}C, Hum: {kelembapan}%"
            
            # sendto butuh argumen alamat tujuan setiap kali kirim
            sock.sendto(payload.encode('utf-8'), target_addr)
            
            print(f"Sent: {payload}")
            time.sleep(1) # Kirim setiap 1 detik
            
    except KeyboardInterrupt:
        print("\nPengiriman data dihentikan.")
    finally:
        sock.close()

if __name__ == "__main__":
    udp_sender()
