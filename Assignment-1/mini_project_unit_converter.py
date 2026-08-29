# Mini Project: Unit Converter

print("===== UNIT CONVERTER =====")

print("\n1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")
print("3. Kilograms to Pounds")

choice = int(input("\nEnter your choice (1-3): "))

if choice == 1:
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371
    print("Distance in miles:", miles)

elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif choice == 3:
    kg = float(input("Enter weight in kilograms: "))
    pounds = kg * 2.20462
    print("Weight in pounds:", pounds)

else:
    print("Invalid choice.")