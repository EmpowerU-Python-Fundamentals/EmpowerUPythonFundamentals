# def my_func():
#     # "doc my f"
#     a = 1
#     print("test1")
#     print("test2")
#     print("test3")
# print(my_func)
# my_func()
# print("run:", my_func())

# help(print)
# help(my_func)
# print(print.__doc__)
# print(my_func.__doc__)


# def add(a, b):
#     return a+b
#     print("end")
# print(add(10, 5))

# def add(a, b):
#     s = 0
#     for _ in range(a):
#         if s > 10:
#             return s +1
#         s+= b
#     return s

# print(add(10, 5))

# def info(name, age, city):
#     print("="*20)
#     print(f"name: {name}")
#     print(f"age: {age}")
#     print(f"city: {city}")
#     print("="*20)

# # info("liubomyr") #TypeError: info() missing 2 required positional arguments: 'age' and 'city'
# # info("liubomyr", 39) #TypeError: info() missing 1 required positional argument: 'city'
# info("liubomyr", 39, "Lviv") 
# # info("liubomyr", 39, "Lviv", None) #TypeError: info() takes 3 positional arguments but 4 were given



# def info(name, age=39, city="Lviv"):
#     print("="*20)
#     print(f"name: {name}")
#     print(f"age: {age}")
#     print(f"city: {city}")
#     print("="*20)

# # info()#TypeError: info() missing 1 required positional argument: 'name'
# info("liubomyr")
# info("liubomyr", 18)
# info("liubomyr", 18, "Odesa")
# # info("liubomyr", 18, "Odesa", 10 ) #TypeError: info() takes from 1 to 3 positional arguments but 4 were given
# info("liubomyr", "Odesa")
# info(18,  "Odesa", "liubomyr")
# info(age=18,  city="Odesa", name="liubomyr")

# def info(name, age=39, a,  city="Lviv"): pass #SyntaxError: parameter without a default follows parameter with a default


# def f(l=[]):
#     l.append(1)
#     print(l)

# f([1,2,3])    
# f([1,2,3, 4])  
# ll = [9,8,7,6]  
# f(ll)
# print(f"{ll=}")
# f()
# f()
# f([1,2,3, 4])  
# f()
# f()

# def f(l=None):
#     if l is None:
#         l = []
#     l.append(1)
#     print(l)

# f([1,2,3])    
# f([1,2,3, 4])  
# ll = [9,8,7,6]  
# f(ll)
# print(f"{ll=}")
# f()
# f()
# f([1,2,3, 4])  
# f()
# f()

# def f(*args):
#     print(f"{args=}")

# f(1 , 2,3,4,5,6)
# f(1, 9, 8)

# def f(**kwargs):
#     print(f"{kwargs=}")

# f(a=1 , b=22, c=3)

# def f(a, b, *args, key_1=1, key_2 = 2, **kwargs):
#     print(f"{a=} {b=} {args=} {key_1=} {key_2=} {kwargs=}")
# f(1,2,3,4,5,6,7, key_1=25, key_3=99)
# f(1,2)

# print(dir())
# def f():
#     print(f"in func {dir()}")
#     a = 10
#     b=20
#     print(f"in func {dir()}")
    

# print(dir())
# f()
# print(dir())
# # print(a) #NameError: name 'a' is not defined

# TEXT = "python"
# LIST = ["python", "C++"]
# def f():
#     LIST.append(1)
#     TEXT = 10
#     print(TEXT)
#     print(LIST)

# f()
# print(TEXT)
# print(LIST)

# TEXT = "python"
# LIST = ["python", "C++"]
# def f():
#     print(TEXT) #UnboundLocalError: cannot access local variable 'TEXT' where it is not associated with a value
#     LIST.append(1)
#     TEXT = 10
#     print(TEXT)
#     print(LIST)
# print("=>>")
# f()
# print(TEXT)
# print(LIST)


# TEXT = "python"
# LIST = ["python", "C++"]
# def f():
#     global TEXT
#     print(TEXT) #UnboundLocalError: cannot access local variable 'TEXT' where it is not associated with a value
#     LIST.append(1)
#     TEXT = 10
#     print(TEXT)
#     print(LIST)
# print("=>>")
# f()
# print(TEXT)
# print(LIST)

# text = "python"
# def f():
#     nonlocal text #SyntaxError: no binding for nonlocal 'text' found
#     text = 10
#     print(text)
# print(text)

# def f(name):
#     local_name = name
#     def l():
#         print(local_name)
#     l()

# f("test_1")
# f("test_2")
# def f(name):
#     local_name = name
#     def l(text):
#         nonlocal local_name
#         local_name += text 
#         print(local_name)

#     return l

# f1 = f("test_1")
# f2 = f("test_2")

# f1("10")
# f2("20")
# f2("20")
# f2("aa")
# f2("20")


# def rec(n=0):
#     print(f"run rec({n})")
#     return rec(n+1)
# # import sys
# # sys.setrecursionlimit(10000)
# rec(0)

# 7! 1*2*3*4*5*6*7
# def fuc_1(n):
#     result = 1
#     for i in range(1,n+1):
#         result = result*i
#     return result
# print(fuc_1(5))
# print(fuc_1(6))
# print(fuc_1(7))

# def fuc_1(n):
#     if n == 0:
#         return 1
#     return n*fuc_1(n-1)
# print(fuc_1(5))
# print(fuc_1(6))
# print(fuc_1(7))

# nested_dict = {
#         "рівень_1_ключ_1": {
#             "рівень_2_ключ_1": {
#                 "рівень_3_ключ_1": "рядок тексту",  # Рядок (string)
#                 "рівень_3_ключ_2": 123,             # Ціле число (integer)
#                 "рівень_3_ключ_3": 45.67            # Число з плаваючою комою (float)
#             },
#             "рівень_2_ключ_2": True,                # Булеве значення (boolean)
#             "рівень_2_ключ_3": None                 # NoneType
#         },
#         "рівень_1_ключ_2": [
#             "елемент_списку_1",                     # Список (list)
#             {"вкладений_словник_в_списку": 789}
#         ],
#         "рівень_1_ключ_3": ("кортеж_елемент_1", False) # Кортеж (tuple)
#     }

# print(nested_dict)

# print("="*20)
# def print_dict(d, level=0):

#     for key, value in d.items():
#         if type(value) in (dict, ):
#             print(f"{'\t'*level}{key}:")
#             print_dict(value, level=level+1)
#         else:
#             print(f"{'\t'*level}{key}:{value}")
# print_dict(nested_dict)


# def add(a,b):
#     return a+b

# add2 = lambda a,b : a+b

# print(f"{add(3,7) =}")
# print(f"{add2(3,7) =}")

# def cond(element):
#     if type(element) in (int, float):
#         return element
#     elif type(element) is str:
#         return len(element)
#     return 0

# l = [1, '10',2, "test", 18, 999, [1,2,3,4], (4,5)]
# l.sort(key=cond)
# print(l)
# l.sort(key=lambda e: -e if type(e) in (int, float) else -len(e) if type(e) is str else 0 )
# print(l)

# def f(l: list) -> list:
#     # l.append(1)
#     return l+l

# g = f([1,2,3])
# # g.append(10)
# # print(g)
# # print(f(10))
# sum([1,2,3,4])

# print(f"{sum([1,2,3,4])}")
# print(f"{sum([1,2,3,4])      =}")
# print(f"sum([1,2,3,4])={sum([1,2,3,4])}")
# from random import randint

# for i in range(10):
#     s = [randint(0, 100) for _ in range(5)]
#     print(f"{sum(s)}")
#     print(f"{s}{sum(s) =}")


# TEXT = "python"
# LIST = ["python", "C++"]
# def f():
#     # print(TEXT)
#     print(LIST)
#     # LIST = 10 #UnboundLocalError: cannot access local variable 'LIST' where it is not associated with a value
#     LIST.append(10)
#     TEXT = 10
#     print(TEXT)
#     print(LIST)

# f()




HOST = ""
PORT = 32

# f(HOST, PORT)