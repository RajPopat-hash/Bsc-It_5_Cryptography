def caesar(text, shift):
    result = ""

    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch.lower()) - 97 + shift) % 26 + 97)
        else:
            result += ch

    return result

text = input("Enter text: ")
shift = int(input("Enter shift: "))

print("Encrypted text =", caesar(text, shift))
