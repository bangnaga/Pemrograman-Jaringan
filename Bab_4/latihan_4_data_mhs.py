# Credit: Fikom UIT
mahasiswa = []

def tambah_mhs(nama, nim):
    mhs = {"nama": nama, "nim": nim}
    mahasiswa.append(mhs)

def tampilkan_semua():
    print(f"--- Data Mahasiswa ({len(mahasiswa)} orang) ---")
    for m in mahasiswa:
        print(f"NIM: {m['nim']} - Nama: {m['nama']}")

if __name__ == "__main__":
    tambah_mhs("Andi", "A11.2025.001")
    tambah_mhs("Budi", "A11.2025.002")
    tampilkan_semua()
