from cryptography.fernet import Fernet


with open('fernet_key.txt', 'r') as f:
    key = f.read()
crypter = Fernet(key)

with open('encrypted_hacked.jpg', 'rb') as f:
    data = f.read()

with open('decrypted_hacked.jpg', 'wb') as f:
    decrypt_data = crypter.decrypt(data)
    f.write(decrypt_data)
    print('> Decrypted <')