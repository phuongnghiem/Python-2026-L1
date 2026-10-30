def print_star(m,n):
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m-1 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()



a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
print_star(a,b)
