def get_divisors(number):
	if number <= 0:
		raise ValueError("The number must be positive")

	return [divisor for divisor in range(1, number + 1)
			if number % divisor == 0]


print(get_divisors(12))
