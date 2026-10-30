def remove_dollar_sign(s ):
    return s.replace("$","")

n = input("Enter: ")
new_string = remove_dollar_sign(n)
print(new_string)

def remove_dollar_sign2(s ):
    out = " "
    for c in s:
        if c == "$":
            out = out + c


print(remove_dollar_sign2("Hellooooooooooooooooo$3$j#k#$"))