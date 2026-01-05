# Credit: Fikom UIT
import psutil
import time
import socket
import json

# Contoh Kode untuk Opsi B (Monitoring Agent)
# Mengirim data CPU/RAM ke Server Monitoring

SERVER_IP = 'localhost'
SERVER_PORT = 5555

def start_agent():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"Monitoring Agent Started. Sending data to {SERVER_IP}:{SERVER_PORT}")
    
    try:
        while True:
            # Ambil metrics system
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent
            
            data = {
                "hostname": socket.gethostname(),
                "cpu": cpu,
                "ram": ram,
                "disk": disk
            }
            
            # Kirim via UDP (karena data stream cepat)
            msg = json.dumps(data)
            client.sendto(msg.encode(), (SERVER_IP, SERVER_PORT))
            
            print(f"Sent: {msg}")
            
    except KeyboardInterrupt:
        print("Agent Stopped.")

if __name__ == "__main__":
    # pip install psutil
    try:
        start_agent()
    except ImportError:
        print("Module 'psutil' not found. Install: pip install psutil")
