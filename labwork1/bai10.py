def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

n = int(input("Enter a number: "))
print(f"Divisors of {n}: {get_divisors(n)}")