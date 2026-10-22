# Lab 1 - Exercise 11: Compute distance between two points
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Test
if __name__ == "__main__":
    print("Enter coordinates of two points:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    print(f"Distance = {distance(x1, y1, x2, y2)}")
