from cryptography.fernet import Fernet

ENCRYPTION_KEY = b'aWOfZVnlPt0NiEp1YyiAi3E0AgTyTPmxlir0an4H-Bw='

cipher = Fernet(ENCRYPTION_KEY)

with open("received_log.enc", "rb") as f:
    encrypted_data = f.read()

decrypted_data = cipher.decrypt(encrypted_data)

with open("decrypted_logs.txt", "wb") as f:
    f.write(decrypted_data)

print("✅ Decryption complete. Logs saved to decrypted_logs.txt")
