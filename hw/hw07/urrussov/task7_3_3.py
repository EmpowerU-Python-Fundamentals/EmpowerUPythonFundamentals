def filter_words(st):
    """
    Filters and formats a given string by removing extra spaces and capitalizing the first character 
    """
    return " ".join(st.capitalize().split())
