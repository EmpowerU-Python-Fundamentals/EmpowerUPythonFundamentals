# print([i * i for i in range(10) if i % 2])
# print({i + j for i in range(10) for j in range(10)})
# print({i: j for i in range(10) for j in range(10)})
# print( (i+j for i in range(10) for j in range(10)) )

# print(list(zip([1,2,3,4,5], "abcdefgijkl", (10,20,30))))
# print(list(map(int, "1234")))

# def is_pos(number):
#     return number > 0
# print(list(filter(is_pos, [1,-2,3,-4,5,6,7,-8,9])))


# list_number = [25, 739, 48]
# print(f"{id(list_number)=}")
# it = iter(list_number)# list_number.__iter__()
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# # print(it.__next__())
# # print(next(it)) #StopIteration


# class MyRange:
#     def __init__(self, start, end=None, step=1):
#         print(f"__init__ {start=} {end=} {step=}")
#         if end is None:
#             self.end = start
#             self.start = 0
#         else:
#             self.start = start
#             self.end = end
#         self.step = step
#     def __str__(self):
#         return f"MyRange({self.start}, {self.end}, {self.step})"
    
#     def __iter__(self):
#         self.current = self.start
#         return self
#     def __next__(self):
#         current = self.current
#         self.current += self.step
#         if current > self.end:
#             raise StopIteration(f"MyRange StopIteration {self.current}")
#         return current

# r1 = MyRange(5)
# r2 = MyRange(3, 8)
# r3 = MyRange(3, 8, 2)
# print(r1,r2,r3)
# for i in r1:
#     print(i)
#     for j in r2:
#         print("\t", j)
#         for k in r3:
#             print("\t\t", k)


# for N in [i*10 for i in range(1,10)]:
#     l = [i for i in range(N)]
#     g = (i for i in range(N))
#     print(f"{N=}")
#     print(f"\t{l.__sizeof__()=}")
#     print(f"\t{g.__sizeof__()=}")

# def my_gen():
#     print("init body")
#     yield 1
#     yield 2
#     yield 3
#     yield 20
#     yield 10

# print(my_gen)

# g1 = my_gen()
# g2 = my_gen()
# print(g1)
# print(f"{next(g1)=}")
# print(f"{next(g1)=}")
# print(f"{next(g2)=}")
# print(f"{next(g1)=}")
# print(f"{next(g1)=}")
# print(f"{next(g2)=}")
# print(f"{next(g2)=}")
# print(f"{next(g2)=}")
# print(f"{next(g2)=}")
# print(f"{next(g2)=}")

# def my_range(start, end=None, step=1):
#     print(f"run my_range {start=} {end=} {step=}")
#     if end is None:
#         end = start
#         start = 0
#     while start < end:
#         print("start iter")
#         print(f"before yield {start=}")
#         yield start
#         print("after yield")
#         start += step
#         print("end iter")

# r = my_range(10)
# print(r)
# print("*"*10)
# print(f"{next(r)=}")
# print("*"*10)
# print(f"{next(r)=}")
# print("*"*10)
# for i in r:
#     print(i)

# method = [map, reversed, sorted]

# list(map(lambda e: print(e), method))
# def m():
#     raise StopIteration()
# l = [1,2,3,m, 4,5,6,7]
# for i in l:
#     print(type(i))
#     if callable(i):
#         i()
#     print(i)


def get_all_user():
    sql = "SELCT * from USERS"
    users = cursor.execut(sql)
    return users

def get_all_user():
    sql = "SELCT * FROM users"
    # count_max = cursor.execut("SELCT COUNT(*) FROM users")
    count_max = 100
    current = 0
    step = 20
    while current < count_max:
        sql = f"SELCT * FROM users ORDER BY id ASC LIMIT {step} OFSET {current}"
        # users = cursor.execut(sql)
        # yield users
        yield range(current, step)
        current += step

for i in get_all_user():
    print(i)