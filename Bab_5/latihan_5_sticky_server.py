# Credit: Fikom UIT
import socket

def sticky_packet_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen(1)
    print("=== Sticky Packet Server (Delimiter Mode) ===")
    
    conn, addr = server.accept()
    print(f"Connected: {addr}")
    
    # Teknik: Menggunakan makefile() agar bisa pakai readline()
    # Ini cara termudah menangani framing berbasis delimiter '\n'
    socket_file = conn.makefile('r', encoding='utf-8')
    
    conn.settimeout(10.0) # Jika 10 detik diam, anggap putus
    
    try:
        while True:
            # readline() akan terus membaca sampai ketemu '\n'
            # Ini otomatis menangani fragmentasi atau penggabungan paket
            line = socket_file.readline()
            
            if not line:
                break # Koneksi putus
                
            # Hilangkan whitespace/newline di ujung
            cleaned_msg = line.strip()
            print(f"Terima Pesan Utuh: {cleaned_msg}")
            
            # Kirim balasan juga harus pakai delimiter
            conn.send(f"ACK: {cleaned_msg}\n".encode('utf-8'))
            
    except socket.timeout:
        print("Timeout! Client terlalu lama diam.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        socket_file.close() # Penting menutup reader wrapper
        conn.close()
        server.close()

if __name__ == "__main__":
    sticky_packet_server()
