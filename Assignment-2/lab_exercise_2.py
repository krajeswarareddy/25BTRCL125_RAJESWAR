# Lab Exercise 2: Prime Number and Factorial Programs

# ---------- Prime Number ----------
print("===== PRIME NUMBER CHECK =====")

n = int(input("Enter a number: "))

if n < 2:
    print("The number is not prime.")
else:
    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")


# ---------- Factorial ----------
print("\n===== FACTORIAL =====")

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is:", factorial)