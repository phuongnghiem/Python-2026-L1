colors = ["Blue", "Yellow", "Black", "Red", "White"]
favorite_color = input("What is your favorite color? ")

if favorite_color in colors:
	color_index = colors.index(favorite_color)
	print(f"Your colod is at index {color_index} in my list")
else:
	print("Sorry, I could not find your color")
