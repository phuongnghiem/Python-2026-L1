number = int(input("Enter a number? "))
is_prime = number >= 2

for divisor in range(2, int(number ** 0.5) + 1):
	if number % divisor == 0:
		is_prime = False
		break

if is_prime:
	print(f"{number} is a prime number")
else:
	print(f"{number} is a NOT prime number")
