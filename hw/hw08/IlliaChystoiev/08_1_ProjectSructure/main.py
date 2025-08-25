from utils import *
from models import *

print('\n', list(filter(lambda s: not ("__" in s), dir())), '\n')

import os

message = input("Ведіть свій комент -> ")
log_in_file(format_string(message))

print("Дані записано в app.log в директорії -> ", os.getcwd(), '\n')