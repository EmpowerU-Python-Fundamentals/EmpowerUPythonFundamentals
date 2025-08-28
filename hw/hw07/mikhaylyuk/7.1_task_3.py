def count_chars(word):
    """
    Повертає словник з кількістю кожного символа 
    word - вхідне слово
    result - словник з кількістю символів
    """
    result = {}
    for ch in word:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result

print(count_chars("hello")) 

# вивід - {'h': 1, 'e': 1, 'l': 2, 'o': 1} 