def print_pattern(m, n):
	if m < 0 or n < 0:
		raise ValueError("m and n must be non-negative")

	for _ in range(m):
		print("*" * n)


print_pattern(3, 5)
