import hashlib

text = input("Enter text: ")

result = hashlib.sha1(text.encode())
print("SHA1 =", result.hexdigest())
