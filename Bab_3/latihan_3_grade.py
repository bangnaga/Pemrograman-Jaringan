# Credit: Fikom UIT
def cek_grade(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    else:
        return "D"

if __name__ == "__main__":
    n = int(input("Masukkan Nilai Angka: "))
    print(f"Grade Anda: {cek_grade(n)}")
