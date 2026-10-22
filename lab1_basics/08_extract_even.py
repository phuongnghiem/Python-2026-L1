def extract_even(l):
    return [x for x in l if x % 2 == 0]

if __name__ == "__main__":
    example = [1, 4, 5, -1, 10]
    print("Input:", example)
    print("Even numbers:", extract_even(example))
