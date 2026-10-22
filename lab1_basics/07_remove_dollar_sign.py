

def remove_dollar_sign(s):
    return s.replace("$", "")

# Test
if __name__ == "__main__":
    test_str = input("Enter a string with $: ")
    print(remove_dollar_sign(test_str))
