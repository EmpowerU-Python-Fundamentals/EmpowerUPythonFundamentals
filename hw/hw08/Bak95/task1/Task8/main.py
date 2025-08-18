from utils import *
from models import *

# Перевірка, що всі функції імпортувалися коректно
print(list(filter(lambda s: not s.startswith('__'), dir())))
