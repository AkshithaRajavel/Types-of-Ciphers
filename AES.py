from Crypto.Cipher import AES

def AES_encrypt(plain_text,key):
    key = bytes(key,'utf-8')
    plain_text = bytes(key,'utf-8')
    cipher_text = AES.new(key, AES.MODE_ECB)
    return cipher_text.encrypt_and_digest(data)