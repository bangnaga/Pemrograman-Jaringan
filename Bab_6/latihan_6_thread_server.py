# Credit: Fikom UIT
import socket
import threading

# Global variables
CLIENTS = [] # Menyimpan daftar koneksi aktif
LOCK = threading.Lock() # Untuk mencegah race condition saat akses list

def broadcast(message, sender_conn=None):
    """
    Mengirim pesan ke SEMUA client yang terhubung,
    kecuali si pengirim (opsional).
    """
    with LOCK: # Kunci akses agar tidak bentrok
        for conn in CLIENTS:
            if conn != sender_conn:
                try:
                    conn.send(message)
                except:
                    # Jika gagal kirim, mungkin koneksi sudah putus/rusak
                    conn.close()
                    # Kita remove nanti atau biarkan handle_client yang urus
                    pass

def handle_client(conn, addr):
    """
    Fungsi yang akan dijalankan oleh setiap Thread.
    Menangani komunikasi unik dengan satu client.
    """
    print(f"[NEW] {addr} connected.")
    
    # Masukkan ke daftar global
    with LOCK:
        CLIENTS.append(conn)
        
    broadcast(f"\n[INFO] {addr} bergabung ke chat room!\n".encode('utf-8'), conn)
    
    try:
        conn.send("Selamat datang di Fikom Chat Room!\n".encode('utf-8'))
        while True:
            data = conn.recv(1024)
            if not data:
                break # Client putus
            
            msg = data.decode('utf-8')
            # Format pesan broadast
            final_msg = f"[{addr[1]}] says: {msg}"
            broadcast(final_msg.encode('utf-8'), conn)
            
    except Exception as e:
        print(f"[ERR] {addr}: {e}")
    finally:
        # Bersih-bersih saat client disconnect
        with LOCK:
            if conn in CLIENTS:
                CLIENTS.remove(conn)
        
        broadcast(f"\ninfo: {addr} telah keluar.\n".encode('utf-8'))
        conn.close()
        print(f"[DISCONNECT] {addr} disconnected.")

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # SO_REUSEADDR agar port langsung bisa dipakai lagi setelah stop
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server.bind(('0.0.0.0', 6000)) # Port 6000
    server.listen(5)
    print("=== Multi-Threaded Chat Server Running on Port 6000 ===")
    
    while True:
        # Main Thread hanya fokus menerima tamu
        conn, addr = server.accept()
        
        # Buat thread baru untuk melayani tamu tersebut
        # target=fungsi yg dijalankan, args=argumen fungsi tsb
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    run_server()
