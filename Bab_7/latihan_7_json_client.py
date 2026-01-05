# Credit: Fikom UIT
import socket
import json

def json_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect(('localhost', 7000))
        
        print("Menu Request:")
        print("1. Cari Mahasiswa (101, 102, 103)")
        nim_input = input("Masukkan NIM: ")
        
        # Buat Dictionary Request
        request_packet = {
            "command": "GET_MHS",
            "nim": nim_input
        }
        
        # Serialisasi ke String JSON
        json_str = json.dumps(request_packet)
        
        # Kirim
        client.send(json_str.encode('utf-8'))
        
        # Terima Balasan
        raw_response = client.recv(4096).decode('utf-8')
        
        # Deserialisasi Balasan
        response_dict = json.loads(raw_response)
        
        print("\n--- Respon Server ---")
        if response_dict['status'] == 'OK':
            mhs = response_dict['data']
            print(f"Nama : {mhs['nama']}")
            print(f"Prodi: {mhs['prodi']}")
            print(f"IPK  : {mhs['ipk']}")
        else:
            print(f"Error: {response_dict.get('msg')}")
            
    except Exception as e:
        print(f"Error connection: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    json_client()
