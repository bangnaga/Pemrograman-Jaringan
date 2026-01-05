# Credit: Fikom UIT
import socket

def check_net_info():
    print("--- Network Information Tool ---")
    try:
        # Mengambil Hostname (Nama Komputer)
        hostname = socket.gethostname()
        
        # Mengambil IP Address Lokal komputer ini
        # Note: Ini biasanya mengambil IP interface utama
        ip_address = socket.gethostbyname(hostname)
        
        print(f"Hostname  : {hostname}")
        print(f"IP Address: {ip_address}")
        
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    check_net_info()
