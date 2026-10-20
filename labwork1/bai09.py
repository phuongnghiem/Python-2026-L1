def factorial(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
print(f"{n}! = {factorial(n)}")