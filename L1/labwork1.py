# Labwork 1: Python Basics (Gộp các bài tập cơ bản)

def ex1():
    print("\n--- Exercise 1: Circle Area ---")
    radius = float(input("Enter circle radius? "))
    area = 3.14 * radius ** 2
    print(f"Circle area = {area}")

def ex2():
    print("\n--- Exercise 2: Celsius to Fahrenheit ---")
    celsius = float(input("Enter the temperature in Celsius? "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius:g} (C) = {fahrenheit} (F)")

def ex3():
    print("\n--- Exercise 3: Prime Number Check ---")
    number = int(input("Enter a number? "))
    is_prime = number >= 2
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is a NOT prime number")

def ex4():
    print("\n--- Exercise 4: Perfect Number Check ---")
    number = int(input("Enter a number? "))
    divisor_sum = 0
    for divisor in range(1, number // 2 + 1):
        if number % divisor == 0:
            divisor_sum += divisor
    if divisor_sum == number:
        print(f"{number} is a perfect number")
    else:
        print(f"{number} is a NOT perfect number")

def ex5():
    print("\n--- Exercise 5: Favorite Color Index ---")
    colors = ["Blue", "Yellow", "Black", "Red", "White"]
    favorite_color = input("What is your favorite color? ")
    if favorite_color in colors:
        color_index = colors.index(favorite_color)
        print(f"Your color is at index {color_index} in my list")
    else:
        print("Sorry, I could not find your color")

def ex6():
    print("\n--- Exercise 6: Range Operations ---")
    range1 = range(7)
    range2 = range(1, 11, 3)
    range3 = range(5, 0, -1)
    range4 = range(6, -3, -2)

    print(f"range1 {', '.join(map(str, range1))}")
    print(f"range2 {', '.join(map(str, range2))}")
    print(f"range3 {', '.join(map(str, range3))}")
    print(f"range4 {', '.join(map(str, range4))}")

def ex7():
    print("\n--- Exercise 7: Remove Dollar Sign ---")
    def remove_dollar_sign(s):
        return s.replace("$", "")
    text = input("Enter a string? ")
    print(f"Result: {remove_dollar_sign(text)}")

def ex8():
    print("\n--- Exercise 8: Extract Even Numbers ---")
    def extract_even(l):
        return [number for number in l if number % 2 == 0]
    numbers = [1, 4, 5, -1, 10]
    print(f"Original list: {numbers}")
    print(f"Even numbers: {extract_even(numbers)}")

def ex9():
    print("\n--- Exercise 9: Factorial ---")
    def factorial(number):
        if number < 0:
            raise ValueError("The number must be non-negative")
        result = 1
        for value in range(1, number + 1):
            result *= value
        return result
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} = {factorial(num)}")

def ex12():
    print("\n--- Exercise 12: Print Pattern ---")
    def print_pattern(m, n):
        if m < 0 or n < 0:
            raise ValueError("m and n must be non-negative")
        for _ in range(m):
            print("*" * n)
    m = int(input("Enter rows (m): "))
    n = int(input("Enter columns (n): "))
    print_pattern(m, n)

def main():
    while True:
        print("\n" + "="*35)
        print("    LABWORK 1: PYTHON BASICS MENU")
        print("="*35)
        print("1. Ex1: Circle Area")
        print("2. Ex2: Celsius to Fahrenheit")
        print("3. Ex3: Prime Number Check")
        print("4. Ex4: Perfect Number Check")
        print("5. Ex5: Color List Search")
        print("6. Ex6: Range Operations")
        print("7. Ex7: Remove Dollar Sign")
        print("8. Ex8: Extract Even Numbers")
        print("9. Ex9: Factorial Calculation")
        print("12. Ex12: Print Pattern")
        print("0. Exit")
        print("="*35)
        
        choice = input("Select exercise to test (0-12): ").strip()
        
        if choice == '1': ex1()
        elif choice == '2': ex2()
        elif choice == '3': ex3()
        elif choice == '4': ex4()
        elif choice == '5': ex5()
        elif choice == '6': ex6()
        elif choice == '7': ex7()
        elif choice == '8': ex8()
        elif choice == '9': ex9()
        elif choice == '12': ex12()
        elif choice == '0':
            print("Exiting Labwork 1...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()