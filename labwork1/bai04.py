def is_perfect(n):
    if n < 1:
        return False
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n

n = int(input("Enter a number? "))
if is_perfect(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is a NOT perfect number")