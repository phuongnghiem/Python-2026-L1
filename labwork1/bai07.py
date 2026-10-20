def remove_dollar_sign(s):
    return s.replace("$", "")

text = input("Enter a string: ")
print(remove_dollar_sign(text))