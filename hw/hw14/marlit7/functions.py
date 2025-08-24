def greeting_by_name(name):
    return f"Hello {name}!"


def get_symbol_position(text, symbol):
    if len(symbol) > 1:
        return "Error! Symbol can be string with only one letter"
    index = text.find(symbol)
    if index > -1:
        return index + 1
    return "Not found"


def merge(dict1, dict2):
    new_dict = dict1.copy()
    new_dict.update(dict2)
    return new_dict

