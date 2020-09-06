from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64




print('> Encryption <\n')
public_key = RSA.import_key(open('public.pem').read())

with open ('fernet_key.txt', 'rb') as f:
    fernet_key = f.read()

public_crypter = PKCS1_OAEP.new(public_key)

with open ('encrypted_fernet_key.txt', 'wb') as f:
    encrypted_fernet_key = public_crypter.encrypt(fernet_key)
    f.write(encrypted_fernet_key)


print(f'> Public Key: {public_key}')
print(f'> Fernet Key: {fernet_key}')
print(f'> Public Encrypter: {public_crypter}')
print(f'> Encyrpted Fernet Key: {encrypted_fernet_key}')
print('\n>Encryption Completed\n')