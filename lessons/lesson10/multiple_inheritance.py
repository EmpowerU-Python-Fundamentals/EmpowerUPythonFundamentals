# class x: 
#     def f(self): 
#         print("f from x")
# class Y: 
#     def f(self): 
#         print("f from Y")
# class Z: 
#     def f(self): 
#         print("f from Z")

# class A(x, Y): pass
# class B(Y, Z): pass

# class C(x, Z): pass

# class D(C, A, B): 
#     def g(self):
#         super(A, self).f()
#         print("g from D")


# d = D()
# d.f()
# from pprint import pprint
# pprint(D.__mro__)  # Method Resolution Order
# # d.g()


# class User:
#     count = 0
#     __slots__ = ('username', 'email')
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#         User.count += 1

#     def display_info(self, show_email=True):
#         print(f">> Username: {self.username}")
#         if show_email:
#             print(f">> Email: {self.email}")

# user = User("john_doe", "   john@example.com   ")
# user.display_info()
# user.a = 10  # Adding an attribute not in __slots__ will raise an AttributeError


# class Demo:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Demo.count += 1
    
#     @classmethod
#     def get_count(cls):
#         print(f"{cls =}")
#         return cls.count
    
#     def print_name(self):
#         print(f"{self =}")
#         print(f"Name: {self.name}")

    
# d = Demo("example")
# d.print_name() 
# # Demo.print_name() #TypeError: Demo.print_name() missing 1 required positional argument: 'self'
# Demo.print_name(d) #TypeError: Demo.print_name() missing 1 required positional argument: 'self'
# print(d.get_count())  # Accessing class method to get count
# Demo.get_count()  # Accessing class method to get count


# class SQL:

#     def __init__(self, name=None):
#         print(f"Creating SQL instance with name: {name}")
#         self.name = name
#     @classmethod
#     def get_all(cls):
#         print(f"SELECT * FROM {cls.__name__}")
#         return cls


    
#     @staticmethod
#     def get_by_id(table,id):
#         print(f"SELECT * FROM {table} WHERE id = {id}")


# class User(SQL):pass
# class Order(SQL):pass


# print(Order.get_all() ) # Outputs: SELECT * FROM Order
# print(User.get_all())  # Outputs: SELECT * FROM User
# User.get_by_id("User", 1)  # Outputs: SELECT * FROM User WHERE id = 1
# Order.get_by_id("Order", 2)  # Outputs: SELECT * FROM Order WHERE
# u = User()
# u.get_all()  # Outputs: SELECT * FROM User
# u.get_by_id("User", 3)  # Outputs: SELECT * FROM User WHERE id = 3
# u.get_by_id("Order", 3)  # Outputs: SELECT * FROM User WHERE id = 3
# def QQQ():pass

# SQL().get_all()("Test")  # Outputs: SELECT * FROM SQL


# class A(int):
#     def __init__(self, value):
#         super().__init__(value)
#         print(f"Creating instance of A with value: {value}")


class Range:
    def __init__(self, start, end=None, step=1):
        if end is None:
            self.end = start
            self.start = 0
        else:
    
            self.start = start
            self.end = end
        self.step = step

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
        

r = Range(5)
for i in r:
    print(i)  # Outputs: 0, 1, 2, 3, 4

class MyString(str): pass


s = MyString("Hello, World!")
print(s)  # Outputs: Hello, World!
print(s[1:5])  # Outputs: ello
