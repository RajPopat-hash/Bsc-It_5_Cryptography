def otp(text, key):
    result = ""

    for i in range(len(text)):
        result += chr((ord(text[i]) - 65 + ord(key[i]) - 65) % 26 + 65)

    return result

text = input("Enter text: ").upper()
key = input("Enter key: ").upper()

print("Encrypted text =", otp(text, key))
