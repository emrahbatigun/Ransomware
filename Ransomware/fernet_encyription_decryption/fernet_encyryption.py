from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
crypter = Fernet(key)

with open('fernet_key.txt', 'wb') as f:
    f.write(key)

with open('hacked.jpg', 'rb') as f:
    data = f.read()
    with open('encrypted_hacked.jpg', 'wb') as f:
        crypt_data = crypter.encrypt(data)
        f.write(crypt_data)
    print(' > Encyrpyted <')

