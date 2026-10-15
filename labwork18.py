def extract_even(I):
	result = []
	for x in I:
	   if x % 2 == 0:
		result.append(x)
	return result

list = [1,2,3,4,5,6,7,8,9,10]
new = extract_event(list)
print(new)	
