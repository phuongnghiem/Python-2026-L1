#1
r=float(input("Enter circle radius:"))
area=3.14*r*r
print("Circle area=", area)
#2
n=float(input("Enter the temperature in Celsius:"))
f=n*9/5 +32
print(f,"F")
#3
n=int(input("Enter n:"))
a=True if n>= 2 else False
for i in range(2,n):
    if n % i == 0:
        a=False
        break
if a== True:
    print("yes")
else:
    print("no")
#4
n = int(input("Enter a number? "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total = total + i

if total == n:
    print(n, "is a perfect number")
else:
    print(n, "is a NOT perfect number")
#5
colors = ["Blue", "Green", "Yellow", "Red", "Black"]

color = input("What is your favorite color? ")

if color in colors:
    print("Your color is at index", colors.index(color), "in my list")
else:
    print("Sorry, I could not find your color")
#6
range1 = range(7)
range2 = range(1, 11, 3)
range3 = range(5, 0, -1)
range4 = range(6, -1, -2)

print("range1:", list(range1))
print("range2:", list(range2))
print("range3:", list(range3))
print("range4:", list(range4))
#7
def remove_dollar_sign(s):
    return s.dell("$")

s = input("Enter a string: ")
print(remove_dollar_sign(s))
#8
def extract_even(l):
    result = []

    for i in l:
        if i % 2 == 0:
            result.append(i)

    return result

l = [1, 4, 5, -1, 10]

print(extract_even(l))
#9
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

n = int(input("Enter a number: "))

print(factorial(n))
#10
def divisors(n):
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result

n = int(input("Enter a number: "))

print(divisors(n))
#11
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Distance =", distance)
#12
def pattern(m, n):
    for i in range(m):
        for j in range(n):
            print("*", end=" ")
        print()

m = int(input("Enter m: "))
n = int(input("Enter n: "))

pattern(m, n)