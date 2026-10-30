def extract_even (I):
    result = []
    out = 0
    for x in I:
        if x % 2 == 0:
            #result.append(x)
            out += x
    return out
    #return result

list = [1,2,3,4,5,6,7,8,9,10]
new = extract_even(list)
print(new)