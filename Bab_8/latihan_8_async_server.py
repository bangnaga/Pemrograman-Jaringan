# Credit: Fikom UIT
import asyncio
import socket

# Asyncio membutuhkan definisi fungsi dengan 'async def'
async def handle_client(reader, writer):
    # Dapatkan alamat client
    addr = writer.get_extra_info('peername')
    print(f"[NEW] {addr} connected.")
    
    writer.write(f"Halo {addr}, selamat datang di Async Server!\n".encode())
    await writer.drain() # Pastikan data terkirim
    
    try:
        while True:
            # await: "Tunggu data masuk, tapi sambil nunggu, kerjakan yang lain"
            data = await reader.read(100)
            if not data:
                break
            
            message = data.decode().strip()
            print(f"[{addr}] Received: {message}")
            
            # Echo balik
            response = f"Echo: {message}\n"
            writer.write(response.encode())
            await writer.drain()
            
    except Exception as e:
        print(f"Error {addr}: {e}")
    finally:
        print(f"[CLOSE] {addr} closed.")
        writer.close()
        await writer.wait_closed()

async def main():
    # Membuat server dengan API High-Level asyncio
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888)

    addr = server.sockets[0].getsockname()
    print(f'=== Asyncio Server Serving on {addr} ===')

    # Server forever loop
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        # Menjalankan Event Loop
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer Stopped.")
