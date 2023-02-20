#from Cryptodome.Cipher import AES
import uuid
import base64
from cryptography.fernet import Fernet

def mac_address():
    return str(uuid.getnode())

def encrypt(text ,directory):        
    token = f.encrypt(text.encode())
    
    with open(directory, 'wb') as file:
        file.write(token)

def decrypt(directory):
    with open(directory, 'rb') as file:
        return f.decrypt(file.read()).decode()
    
b = base64.urlsafe_b64encode(mac_address().encode().zfill(32))
f = Fernet(b)