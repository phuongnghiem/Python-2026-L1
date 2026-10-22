def is_perfect(n):
    if n <= 1:
        return False
    total = 1  # 1 is always a divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i and n // i != n:
                total += n // i
    return total == n

number = int(input("Enter a number? "))
if is_perfect(number):
    print(f"{number} is a perfect number")
else:
    print(f"{number} is a NOT perfect number")
