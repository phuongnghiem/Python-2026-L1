def print_pattern(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print(" ".join("*" for _ in range(n)))
        else:
            print("*" + " " * (2 * (n - 2) + 1) + "*")

m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))
print_pattern(m, n)