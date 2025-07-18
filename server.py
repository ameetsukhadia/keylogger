from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_data()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"logs/log_{timestamp}.enc"
    
    with open(filename, "wb") as f:
        f.write(data)
    
    print(f"[+] Log received and saved as {filename} | Size: {len(data)} bytes")
    return 'OK'

if __name__ == '__main__':
    import os
    os.makedirs("logs", exist_ok=True)
    app.run(host="0.0.0.0", port=5000)
