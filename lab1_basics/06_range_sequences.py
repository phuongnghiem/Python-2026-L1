print("Name\tSequence")
print("range1\t", end="")
print(", ".join(str(i) for i in range(0, 7)))

print("range2\t", end="")
print(", ".join(str(i) for i in range(1, 11, 3)))

print("range3\t", end="")
print(", ".join(str(i) for i in range(5, 0, -1)))

print("range4\t", end="")
print(", ".join(str(i) for i in range(6, -3, -2)))
