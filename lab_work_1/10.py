def divisors_of_n(n):
    divisors = []

    for i in range(1,n+1):
        if n % i == 0:
            divisors.append(i)

    return divisors

a = int(input("Enter the number: "))
print(divisors_of_n(a))

