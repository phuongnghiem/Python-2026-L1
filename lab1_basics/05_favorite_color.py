# Lab 1 - Exercise 5: Find favorite color in a list

colors = ["Blue", "Yellow", "Green", "Red", "Purple", "Orange"]  # index 3 is Red

favorite = input("What is your favorite color? ")

found = False
for i, color in enumerate(colors):
    if color.lower() == favorite.lower():
        print(f"Your color is at index {i} in my list")
        found = True
        break

if not found:
    print("Sorry, I could not find your color")
