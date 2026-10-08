def factorial(number):
	if number < 0:
		raise ValueError("The number must be non-negative")

	result = 1
	for value in range(1, number + 1):
		result *= value

	return result


print(factorial(5))
