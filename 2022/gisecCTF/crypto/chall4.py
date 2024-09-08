from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode as enc

key = b"Sixteen byte key"
flag = b'GisecCTF{Introduction_to_AES_encryption}'
cipher = AES.new(key,AES.MODE_ECB)
encrypted = enc(cipher.encrypt(pad(flag,16)))
print(encrypted)
