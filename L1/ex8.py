def extract_even(l):
	return [number for number in l if number % 2 == 0]


numbers = [1, 4, 5, -1, 10]
print(extract_even(numbers))
