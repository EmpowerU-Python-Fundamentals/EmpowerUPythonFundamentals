def bool_to_word(boolean):
    try:
        return "Yes" if boolean else "No"
    except TypeError:
        return "No"