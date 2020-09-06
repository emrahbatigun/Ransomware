from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import base64




print('> Decryption <\n')

with open('encrypted_fernet_key.txt', 'rb') as f:
    encryted_fernet_key = f.read()

private_key = RSA.import_key(open('private.pem').read())

private_crypter = PKCS1_OAEP.new(private_key)

decrypted_fernet_key = private_crypter.decrypt(encryted_fernet_key)

with open('decrypted_fernet_key.txt', 'wb') as f:
    f.write(decrypted_fernet_key)

print(f'>Private Key: {private_key}')
print(f'>Private Decyrpter: {private_crypter}')
print(f'>Decrypted Fernet Key: {decrypted_fernet_key}')
print('\n> Decryption Completed <')