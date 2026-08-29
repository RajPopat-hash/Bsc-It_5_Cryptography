def rail_fence(text, rails):
    result = ""

    for row in range(rails):
        result += text[row::2 * (rails - 1)]

    return result

text = input("Enter text: ")
rails = int(input("Enter number of rails: "))

print("Encrypted text =", rail_fence(text, rails))
