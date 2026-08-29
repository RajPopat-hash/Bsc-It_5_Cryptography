def diffie_hellman(p, g, a, b):
    A = (g ** a) % p
    B = (g ** b) % p

    key1 = (B ** a) % p
    key2 = (A ** b) % p

    return A, B, key1, key2

p = 23
g = 5
a = 6
b = 15

A, B, key1, key2 = diffie_hellman(p, g, a, b)

print("Public key of A =", A)
print("Public key of B =", B)
print("Shared key of A =", key1)
print("Shared key of B =", key2)
