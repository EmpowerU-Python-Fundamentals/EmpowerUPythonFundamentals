def count_characters(text):
    """Count the number of occurrences of each character in a string."""
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result

def main():
    user_input = input("Enter a string: ")
    counts = count_characters(user_input)
    print(counts)

if __name__ == "__main__":
    main()