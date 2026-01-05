# Credit: Fikom UIT
import threading
import time

def worker(nama):
    print(f"Worker {nama} mulai...")
    time.sleep(2)
    print(f"Worker {nama} selesai.")

t1 = threading.Thread(target=worker, args=("A",))
t2 = threading.Thread(target=worker, args=("B",))

t1.start()
t2.start()
