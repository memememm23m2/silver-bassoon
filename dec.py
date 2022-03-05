from cryptography.fernet import Fernet

fernet = Fernet(input("Key: "))

with open('main.py', 'rb') as enc_file:
    encrypted = enc_file.read()

decrypted = fernet.decrypt(encrypted)

with open('main.py', 'wb') as dec_file:
    dec_file.write(decrypted)
