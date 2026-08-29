# Lab Exercise 2: Variables, Operators, and Input/Output

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n--- Arithmetic Operators ---")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

print("\n--- Relational Operators ---")
print("a == b:", a == b)
print("a > b:", a > b)
print("a < b:", a < b)

print("\n--- Logical Operators ---")
print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0:", a > 0 or b > 0)
print("not (a > b):", not (a > b))

print("\n--- Assignment Operator ---")
c = a
c += b
print("c after c += b:", c)

print("\n--- Bitwise Operators ---")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)