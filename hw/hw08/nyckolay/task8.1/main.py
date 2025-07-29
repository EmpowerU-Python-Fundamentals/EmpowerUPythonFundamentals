"""08.1 Practical tasks. import practice ''" """

from utils import *
from models import *
print(list(filter(lambda str: not ("__" in str), dir())))

create_admin()
