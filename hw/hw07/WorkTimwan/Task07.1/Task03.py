word = input("enter the word ")

l = list(word)

counter  = {}




for letter in l:
    if letter not in counter:
        counter[letter] = l.count(letter)
print(counter)

        
        

