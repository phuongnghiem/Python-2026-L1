def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*i
    print(factorial)

i = int(input("Enter the number: "))
factorial(i)