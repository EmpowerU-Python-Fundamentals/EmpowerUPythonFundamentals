# # def add_tag(tag):
# #     def decorator(func):
# #         def wrapper(*args, **kwargs):
# #             res = func(*args, **kwargs)
# #             return f"{tag}{res}{tag}"
# #         return wrapper
# #     return decorator
# #
# #
# #
# # @add_tag("<strong>")
# # def get_message():
# #     return "Hello, World!"
# #
# # print(get_message())
#
#
#
# # def fibonacci_numbers():
# #        x = 0
# #        y = 1
# #        step = 0
# #        lst = [x,y]
# #        res = sum(lst[0:1])
# #        print(res)
#
#
# # def fibonacci_numbers():
# #     x, y = 0, 1
# #     while True:
# #         yield x
# #         x, y = y, x + y
#
#
# # def combinations(list1, list2):
# #     for l in list1:
# #         for l2 in list2:
# #             yield l,l2
# #
# #
# # g = combinations([1,2,3], ['a','b','c'])
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
#
# # def far(cls):
# #     lst = []
# #     for c in cls:
# #         f = (c * 9/5) + 32
# #         lst.append(f)
# #     return lst
# # print(far([0, 10, 20, 30, 40]))
#
# # def celsius_to_fahrenheit(temps):
# #     f_lst = [(c * 9/5) + 32 for c in temps]
# #     return f_lst
#
# # def celsius_to_fahrenheit(temps):
# #     f_lst = map(lambda c: (c * 9/5) + 32, temps)
# #     return list(f_lst)
# #
# # nums = [0, 10, 20, 30, 40]
# # res = celsius_to_fahrenheit(nums)
# #
# # print(res)
#
#
#
# #
# # def zp(keys, values):
# #     return {key: value for (key, value) in zip(keys, values)}
# #
# #
# # print(zp([1,2,3,4,5], ['a', 'b', 'c', 'd']))
#
#
# my_var = lambda x: x +1