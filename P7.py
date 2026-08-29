def swap(a, b):
    a, b = b, a
    return a, b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = swap(a, b)

print("After swapping:")
print("First number =", a)
print("Second number =", b)
