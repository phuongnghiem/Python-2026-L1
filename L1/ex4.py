number = int(input("Enter a number? "))
divisor_sum = 0

for divisor in range(1, number // 2 + 1):
	if number % divisor == 0:
		divisor_sum += divisor

if divisor_sum == number:
	print(f"{number} is a perfect number")
else:
	print(f"{number} is a NOT perfect number")
