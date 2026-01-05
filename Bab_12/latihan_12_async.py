# Credit: Fikom UIT
import asyncio

async def sapa_async():
    print("Halo...")
    await asyncio.sleep(1) # Simulasi I/O wait
    print("...Dunia Async!")

if __name__ == "__main__":
    asyncio.run(sapa_async())
