Keylogger with Encrypted Data Exfiltration
A fully functional Educational Keylogger Project with:

 AES Encryption using cryptography

 Remote HTTP Exfiltration using Flask

 Stealth EXE Packaging with PyInstaller

 Decryption Dashboard (HTML) for easy log viewing

 Windows Startup Persistence setup

⚠ Ethical Disclaimer
This project is strictly for educational and ethical penetration testing purposes only. Unauthorized use of keyloggers is illegal and unethical. Use this responsibly in controlled environments.


 Features
Feature	Status
AES Encrypted Keylogs	
Remote HTTP Exfiltration	
Stealth Windows EXE	
Auto Start with Task Scheduler	
HTML Decryption Dashboard	
Clean Multi-log Handling

keylogger_project/
│
├── keylogger_http.py        # Main keylogger script (HTTP exfiltration)
├── server.py                # HTTP server to receive logs
├── decrypt_dashboard.py     # HTML dashboard for decrypting logs
├── generate_key.py          # Generates encryption key
├── requirements.txt         # Dependencies
└── templates/
    └── dashboard.html      
└── logs/                    # (Auto-created) Encrypted log files
└── dist/                    # (Auto-created) PyInstaller EXE



