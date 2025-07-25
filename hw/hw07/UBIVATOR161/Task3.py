def word(x):
    counts = {}
    for char in x:
        if char in counts:
            counts[char] +=1
        else:
            counts[char]=1
    
    return counts
string = input("Enter a string: ")
result = word(string)
print(result)