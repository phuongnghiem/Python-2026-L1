def extract_even(l):
    return [x for x in l if x % 2 == 0]

numbers = [1, 4, 5, -1, 10]
print(extract_even(numbers))   