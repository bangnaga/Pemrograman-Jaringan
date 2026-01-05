# Credit: Fikom UIT
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
    def perkenalan(self):
        print(f"Halo, saya {self.nama}, NIM {self.nim}")

if __name__ == "__main__":
    m1 = Mahasiswa("Siti", "12345")
    m1.perkenalan()
