# Credit: Fikom UIT
def kalkulator():
    print("--- Kalkulator Sederhana ---")
    a = float(input("Angka 1: "))
    b = float(input("Angka 2: "))
    
    print(f"Hasil Tambah: {a + b}")
    print(f"Hasil Kurang: {a - b}")
    print(f"Hasil Kali: {a * b}")
    if b != 0:
        print(f"Hasil Bagi: {a / b}")
    else:
        print("Tidak bisa membagi dengan nol")

if __name__ == "__main__":
    kalkulator()
