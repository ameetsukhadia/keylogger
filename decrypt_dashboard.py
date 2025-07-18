from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# ✅ Replace with your AES Key
ENCRYPTION_KEY = b'aWOfZVnlPt0NiEp1YyiAi3E0AgTyTPmxlir0an4H-Bw='
cipher = Fernet(ENCRYPTION_KEY)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    decrypted_output = ""
    if request.method == 'POST':
        if 'logfile' in request.files:
            file = request.files['logfile']
            encrypted_data = file.read()
            try:
                decrypted_data = cipher.decrypt(encrypted_data)
                decrypted_output = decrypted_data.decode()
            except Exception as e:
                decrypted_output = f"❌ Error decrypting: {e}"
    return render_template('dashboard.html', result=decrypted_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
