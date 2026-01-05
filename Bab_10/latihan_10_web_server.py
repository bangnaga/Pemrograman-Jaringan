# Credit: Fikom UIT
import socket
import os

def run_web_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))
    server.listen(5)
    print("=== Simple Web Server Running on port 8080 ===")
    print("Akses: http://localhost:8080/index.html")

    while True:
        client_sock, addr = server.accept()
        try:
            request = client_sock.recv(1024).decode()
            
            # Parsing baris pertama: "GET /index.html HTTP/1.1"
            headers = request.split('\n')
            first_line = headers[0].split()
            
            if len(first_line) > 1:
                filename = first_line[1] # misal: "/index.html"
                if filename == '/': filename = '/index.html'
                
                # Coba baca file
                # Hilangkan slash depan agar pathnya relatif ke folder ini
                filepath = filename[1:] 
                
                try:
                    with open(filepath, 'r') as f:
                        content = f.read()
                    
                    # HTTP Header
                    response = "HTTP/1.1 200 OK\r\n"
                    response += "Content-Type: text/html\r\n\r\n"
                    response += content
                    
                except FileNotFoundError:
                    # 404 Not Found
                    response = "HTTP/1.1 404 Not Found\r\n\r\n"
                    response += "<h1>404 File Tidak Ditemukan</h1>"
                
                client_sock.sendall(response.encode())
                
        except Exception as e:
            print(f"Error {e}")
        finally:
            client_sock.close()

if __name__ == "__main__":
    # Buat file dummy index.html jika belum ada
    if not os.path.exists('index.html'):
        with open('index.html', 'w') as f:
            f.write("<html><body><h1>Halo dari Python Web Server!</h1></body></html>")
            
    run_web_server()
