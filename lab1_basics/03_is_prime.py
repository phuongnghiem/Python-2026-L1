# Lab 1 - Exercise 3: Check whether a number is prime

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input("Enter a number? "))
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is a NOT prime number")
