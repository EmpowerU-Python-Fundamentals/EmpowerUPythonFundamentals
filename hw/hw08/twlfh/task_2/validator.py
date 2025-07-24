import re

def validate_user_input(user_input):
    """Check if the input is a valid figure name"""
    pattern = r'^(circle|triangle|rectangle)$'
    return re.fullmatch(pattern, user_input.strip().lower()) is not None