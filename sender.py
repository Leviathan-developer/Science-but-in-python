from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# with open("secret.txt","wb") as key_file:
#    key_file.write(key)
# print(key)
with open("secret.txt","rb") as key_file:
    key = key_file.read()
    cipher = Fernet(key)
with open("message.txt","rb") as message_file:
    message = message_file.read()
encrypted = cipher.encrypt(message)
with open("encrypted.txt","wb") as encrypted_file:
    encrypted_file.write(encrypted)
print("Encrypted successfully")
