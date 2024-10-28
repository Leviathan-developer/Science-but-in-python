from cryptography.fernet import Fernet
with open("secret.txt","rb") as key_file:
    key=key_file.read()
    cipher=Fernet(key)
with open("encrypted.txt","rb") as encrypted_file:
    encrypted=encrypted_file.read()
    decrypted=cipher.decrypt(encrypted)
with open("decrypted.txt","wb") as decrypted_file:
    decrypted_file.write(decrypted)
print("Decrypted successfully")