import re
import sys

def class_name_changer(cls, new_name):

    if not new_name.isalnum():
        raise ValueError("Ім'я класу має містити лише буквено-цифрові символи.")

    if not new_name[0].isupper():
        raise ValueError("Ім'я класу має починатися з великої літери.")

    cls.__name__ = new_name
