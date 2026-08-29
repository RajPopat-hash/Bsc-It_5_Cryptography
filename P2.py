def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Display results
print("Addition =", addition(a, b))
print("Subtraction =", subtraction(a, b))
print("Multiplication =", multiplication(a, b))
print("Division =", division(a, b))
