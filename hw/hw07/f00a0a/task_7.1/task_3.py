def count_letters(word):
    """Calculates the number of characters"""
    letter_counts = {}
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    characters = []
    for letter, count in letter_counts.items():
        characters.append(f'"{letter}":{count}')
    
    result = "{" + ", ".join(characters) + "}"
    print(result)

user_word = input("Enter a word: ")
count_letters(user_word)