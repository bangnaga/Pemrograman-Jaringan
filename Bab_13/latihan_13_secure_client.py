# Credit: Fikom UIT
import socket
import ssl

def secure_client():
    # Setup SSL Context untuk client
    # PROTOCOL_TLS_CLIENT memaksa verifikasi sertifikat server
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    
    # Karena kita pakai Self-Signed Certificate, kita harus mematikan verifikasi hostname & loading CA
    # ATAU kita load cert kita sendiri sebagai "Trusted CA"
    context.load_verify_locations('cert.pem')
    # context.check_hostname = False # Opsional jika hostname tidak match

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Wrap socket
    secure_sock = context.wrap_socket(sock, server_hostname='localhost')
    
    try:
        print("Connecting securely...")
        secure_sock.connect(('localhost', 10023))
        
        # Cek versi protokol yang dipakai
        print(f"Connected with {secure_sock.version()}")
        
        secure_sock.send("Rahasia Negara Bos!".encode())
        
        resp = secure_sock.recv(1024).decode()
        print(f"Response: {resp}")
        
    except ssl.SSLCertVerificationError:
        print("Error: Sertifikat Server tidak dipercaya!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        secure_sock.close()

if __name__ == "__main__":
    secure_client()
