# Credit: Fikom UIT
import socket
import select

def run_select_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 9000))
    server_socket.listen(10)
    server_socket.setblocking(False) # Penting! Non-blocking mode

    # Daftar socket yang akan dipantau
    inputs = [server_socket]
    clients = {} # Mapping socket -> addr

    print("=== Select-based Chat Server on Port 9000 ===")

    while True:
        # Panggil select untuk memantau aktivitas I/O
        # readable = daftar socket yang siap di-READ (ada data masuk)
        # writable = daftar socket yang siap di-WRITE (buffer kosong)
        # exceptional = daftar socket yang error
        readable, writable, exceptional = select.select(inputs, [], inputs)

        for s in readable:
            if s is server_socket:
                # Ada koneksi baru
                conn, addr = s.accept()
                conn.setblocking(False)
                inputs.append(conn)
                clients[conn] = addr
                print(f"[NEW] Connection from {addr}")
            else:
                # Ada pesan dari client yang sudah connect
                try:
                    data = s.recv(1024)
                    if data:
                        # Broadcast ke yang lain
                        msg = f"[{clients[s][1]}] {data.decode()}".encode()
                        for target in inputs:
                            if target is not server_socket and target is not s:
                                try:
                                    target.send(msg)
                                except:
                                    target.close()
                                    inputs.remove(target)
                    else:
                        # Data kosong artinya client close
                        print(f"[CLOSE] {clients[s]} disconnected")
                        if s in inputs: inputs.remove(s)
                        s.close()
                        del clients[s]
                except Exception as e:
                    print(f"Error: {e}")
                    if s in inputs: inputs.remove(s)
                    s.close()
                    del clients[s]

if __name__ == "__main__":
    run_select_server()
