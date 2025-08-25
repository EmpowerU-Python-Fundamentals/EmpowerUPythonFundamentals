import re

class ClassRename:
    def __init__(self, new_name):
        self.new_name = new_name

    def get_rename(self):
        return self.new_name

def class_name_changer(cls, new_name):
    if not new_name or not new_name.strip():
        return ValueError('Name not be empty')
    if not re.fullmatch(r'[A-Z][A-Za-z0-9]*', new_name):
        return ValueError('Invalid class format')

    cls.__name__ = new_name
