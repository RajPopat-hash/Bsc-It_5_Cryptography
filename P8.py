import hashlib

text = input("Enter text: ")

result = hashlib.md5(text.encode())
print("MD5 =", result.hexdigest())
