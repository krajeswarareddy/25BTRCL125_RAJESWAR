# Lab Exercise 3: Frequency Counter Using Dictionaries

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

print("\n===== CHARACTER FREQUENCY =====")

for char, count in frequency.items():
    print(char, ":", count)