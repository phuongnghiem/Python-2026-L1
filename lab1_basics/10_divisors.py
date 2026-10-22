# Lab 1 - Exercise 10: Get all divisors of a number

def get_divisors(n):
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Test
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Divisors of {num}: {get_divisors(num)}")
