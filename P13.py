pip install pycryptodome
from Crypto.Cipher import DES

key = b'12345678'

cipher = DES.new(key, DES.MODE_ECB)

text = input("Enter text: ")

# Make text 8 characters
text = text.ljust(8)[:8].encode()

encrypted = cipher.encrypt(text)
print("Encrypted =", encrypted)

decrypted = cipher.decrypt(encrypted)
print("Decrypted =", decrypted.decode().strip())
