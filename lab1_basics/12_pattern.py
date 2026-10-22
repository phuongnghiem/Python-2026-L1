def print_pattern(m, n):
    """Print a hollow rectangle of size m rows x n columns"""
    if m < 1 or n < 1:
        return
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end="    " if j < n - 1 else "")
            else:
                print(" ", end="    " if j < n - 1 else "")
        print()

if __name__ == "__main__":
    rows = int(input("Enter number of rows (m): "))
    cols = int(input("Enter number of columns (n): "))
    print_pattern(rows, cols)
