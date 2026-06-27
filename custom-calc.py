x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
z = str(input("Enter an operation (+, -, *, /, %, **, //): "))
if z == "+":
    print("Addition: " , x+y)
elif z == "-":
    print("Subtraction: " , x-y)
elif z == "*":
    print("Multiplication: " , x*y)
elif z == "/":
    print("Division: " , x/y)
elif z == "%":
    print("Modulus: " , x%y)
elif z == "**":
    print("Exponentiation: " , x**y)
elif z == "//":
    print("Floor Division: " , x//y)
else:
    print("Invalid operation.")
