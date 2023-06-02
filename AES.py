from Crypto.Cipher import AES
key = b'1234455fghdhdfrs'
cipher = AES.new(key, AES.MODE_EAX)
data = 'this is experminet 4 AES'.encode()
nonce = cipher.nonce
ciphertext = cipher.encrypt(data)
print("Cipher text : ", ciphertext)
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print("plaintext ", plaintext)