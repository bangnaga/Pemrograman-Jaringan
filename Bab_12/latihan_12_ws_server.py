# Credit: Fikom UIT
import asyncio
import websockets
import json
import random

# Menyimpan semua client yang terhubung
connected_clients = set()

async def handler(websocket):
    # Register client baru
    connected_clients.add(websocket)
    try:
        print(f"Client terhubung. Total: {len(connected_clients)}")
        
        while True:
            # Simulasi data real-time
            data = {
                "saham_A": random.randint(100, 200),
                "saham_B": random.randint(50, 80),
                "timestamp": asyncio.get_event_loop().time()
            }
            
            # Kirim ke client ini
            await websocket.send(json.dumps(data))
            
            # Delay 1 detik
            await asyncio.sleep(1)
            
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)
        print(f"Client putus. Total: {len(connected_clients)}")

async def main():
    # Start Websocket Server
    # Note: perlu pip install websockets
    try:
        async with websockets.serve(handler, "localhost", 8765):
            print("WS Server running on ws://localhost:8765")
            await asyncio.futures.Future() # Run forever
    except ModuleNotFoundError:
        print("Error: Library 'websockets' belum diinstall.")
        print("Silakan jalankan: pip install websockets")

if __name__ == "__main__":
    asyncio.run(main())
