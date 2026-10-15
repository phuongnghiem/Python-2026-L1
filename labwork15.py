colors = ["red,green,blue,pink,white"]
favorite = input ("what is your favorite colors?")	
if favorite in colors:
	print("index", colors.index(favorite))
else:
	print(" Sorry, I could not find your favorite colors")


