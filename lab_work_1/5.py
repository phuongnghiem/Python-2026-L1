colors = ["red", "green", "blue", "black", "pink", "yellow"]
favorite = input("What is your favorite color?\n")

if favorite in colors:
    print("Index: ",colors.index(favorite))
else:
    print("Sorry, i couldn't find your color")