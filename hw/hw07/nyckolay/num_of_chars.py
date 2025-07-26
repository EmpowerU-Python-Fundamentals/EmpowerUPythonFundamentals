"""07.1 Practical tasks. Task 3 'Number of characters' """

string = input("Enter the string: ").strip().lower()
result = {}

for char in string.lower():
	# result[char] = result.get(char, 0) + 1
    if char in result:
        result[char] += 1
    else:
        result[char] = 1

print(result)
