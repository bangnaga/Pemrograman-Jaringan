# Credit: Fikom UIT
import socket
import json

# Database dummy
DATABASE = {
    "101": {"nama": "Andi Saputra", "prodi": "Informatika", "ipk": 3.75},
    "102": {"nama": "Budi Santoso", "prodi": "Sistem Informasi", "ipk": 3.40},
    "103": {"nama": "Citra Lestari", "prodi": "Informatika", "ipk": 3.90}
}

def json_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 7000))
    server.listen(5)
    print("=== JSON Database Server Running on Port 7000 ===")
    
    while True:
        conn, addr = server.accept()
        print(f"Connection from {addr}")
        
        try:
            # Terima data (asumsi max 4096 bytes)
            raw_data = conn.recv(4096).decode('utf-8')
            if not raw_data:
                continue
                
            print(f"Request Raw: {raw_data}")
            
            # 1. Deserialisasi (String JSON -> Dict Python)
            try:
                request = json.loads(raw_data)
            except json.JSONDecodeError:
                response = {"status": "ERROR", "msg": "Invalid JSON Format"}
                conn.send(json.dumps(response).encode('utf-8'))
                conn.close()
                continue
            
            # 2. Proses Logika
            command = request.get("command")
            nim = request.get("nim")
            
            response = {}
            if command == "GET_MHS":
                data = DATABASE.get(nim)
                if data:
                    response = {"status": "OK", "data": data}
                else:
                    response = {"status": "NOT_FOUND", "msg": f"NIM {nim} tidak ditemukan"}
            else:
                 response = {"status": "ERROR", "msg": "Unknown Command"}
            
            # 3. Serialisasi Balasan (Dict -> JSON String -> Bytes)
            json_reply = json.dumps(response)
            conn.send(json_reply.encode('utf-8'))
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    json_server()
