def number_of_characters_in_string(string):
        """Count the number of occurrences of each character in a given string.
        
            The function converts the input string to lowercase to ensure case-insensitive counting,
            then calculates the frequency of each character in the string.
        
            Parameters:
                string (str): The input string to analyze.
        
            Returns:
                dict: A dictionary where keys are characters and values are the number of times each character appears in the string.
            """        
        string = string.lower()
        char_count = {}
        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count