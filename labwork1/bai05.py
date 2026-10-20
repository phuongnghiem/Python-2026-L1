colors = ["White", "Black", "Blue", "Red", "Green", "Yellow"]

fav = input("What is your favorite color? ")

found = False
for i, c in enumerate(colors):
    if c.lower() == fav.lower():
        print(f"Your color is at index {i} in my list")
        found = True
        break

if not found:
    print("Sorry, I could not find your color")