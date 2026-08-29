import hashlib

text = input("Enter text: ")

result = hashlib.sha512(text.encode())
print("SHA512 =", result.hexdigest())
