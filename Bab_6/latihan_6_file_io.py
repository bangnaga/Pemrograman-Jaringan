# Credit: Fikom UIT
def tulis_log(pesan):
    try:
        with open("log.txt", "a") as f:
            f.write(pesan + "\n")
        print("Log berhasil ditulis.")
    except Exception as e:
        print(f"Gagal menulis file: {e}")

if __name__ == "__main__":
    tulis_log("Sistem dimulai...")
    tulis_log("User login.")
