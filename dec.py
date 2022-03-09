from cryptography.fernet import Fernet
import json

fernet = Fernet(input("Key: "))

with open('encrypted.py', 'rb') as enc_file:
    encrypted = enc_file.read()

decrypted = fernet.decrypt(encrypted)

with open("json.json", "w") as f:

    json.dump({"id" : str(input("User ID: "))}, f)

with open('maine.py', 'wb') as dec_file:
    dec_file.write(decrypted)
