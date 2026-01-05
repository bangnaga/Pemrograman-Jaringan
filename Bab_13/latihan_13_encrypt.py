# Credit: Fikom UIT
from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()
cipher = Fernet(key)

pesan = b"Rahasia Negara"
encrypted = cipher.encrypt(pesan)
print(f"Encrypted: {encrypted}")

decrypted = cipher.decrypt(encrypted)
print(f"Decrypted: {decrypted.decode()}")
