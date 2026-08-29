# Lab Exercise 3: Simple Calculator and Area Calculation

# ---------- Simple Calculator ----------
print("===== SIMPLE CALCULATOR =====")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# ---------- Area Calculation ----------
print("\n===== AREA CALCULATION =====")

# Area of Rectangle
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
rectangle_area = length * width
print("Area of Rectangle:", rectangle_area)

# Area of Circle
radius = float(input("Enter radius of circle: "))
circle_area = 3.14159 * radius * radius
print("Area of Circle:", circle_area)

# Area of Triangle
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
triangle_area = 0.5 * base * height
print("Area of Triangle:", triangle_area)