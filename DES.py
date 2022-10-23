from crypto.Cipher import DES

def DES_encrypt(plain_text,key):
    key = bytes(key,'utf-8')
    plain_text = bytes(key,'utf-8')
    cipher_text = DES.new(key, DES.MODE_ECB)
    return cipher_text.encrypt(plain_text)
